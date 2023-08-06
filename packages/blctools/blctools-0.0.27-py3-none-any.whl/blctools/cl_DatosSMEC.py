from . import dirs
from . import fechas

import gc
import numpy as np
import pandas as pd
import datetime as dt
from pathlib import Path

from .cl_TablasVC import *

__all__ = ['DatosSMEC',]

class DatosSMEC(TablasVC):
    
    def __init__(
        self,
        fecha_i = None,
        fecha_f = None,
        parques = [],
        dir_salida = None,
        cargar_datos_basicos = 'offline',
        cargar_datos_smec=False,
        mensajes=True,
        mensajes_SQL = True,
        ):

        super().__init__(
            cargar_datos_basicos = cargar_datos_basicos,
            parques = parques,
            solo_CROM = False,
            mensajes = mensajes_SQL,
            )

        # Inicialización de parámetros varios
        self.fecha_i = fechas.mes_ant_dia_1() if fecha_i is None else fechas.validar_fecha_hora(fecha_i)
        self.fecha_f = fechas.mes_act_dia_1() if fecha_i is None else fechas.validar_fecha_hora(fecha_f)
        self.dir_salida = dirs.raiz if dir_salida is None else dirs.check_dir(dir_salida)
        
        self.datos_vc = None
        self.datos_prn = None
        
        if cargar_datos_smec:
            self.consultar_datos_vc(
                fecha_i=self.fecha_i,
                fecha_f=self.fecha_f,
                parques=self.parques,
                mensajes=False)

    #
    # Propiedades. Getters y Setters
    #
    @property
    def fecha_i(self):
        return self.__fecha_i
    
    @fecha_i.setter
    def fecha_i(self,val):
        '''Ingresar una fecha para usar como fecha inicial del rango a analizar/pricesar
        Puede ser un objeto datetime.datetime o texto (string)'''
        self.__fecha_i = fechas.validar_fecha_hora(val)

    @property
    def fecha_f(self):
        return self.__fecha_f

    @fecha_f.setter
    def fecha_f(self,val):
        '''Ingresar una fecha para usar como fecha final del rango a analizar/pricesar
        Puede ser un objeto datetime.datetime o texto (string)'''
        self.__fecha_f = fechas.validar_fecha_hora(val)
        
    #
    # Consultas SQL a la BD
    #
    def __get_SQL_date_conditions(self,fecha_i=None,fecha_f=None):
        
        # Validar y configurar fechas
        if (fecha_i is None) and (fecha_f is None):
            return None
        elif (fecha_i is None) and (fecha_f is not None):
            #hacer que fecha_i = fecha_f
            fecha_i = fechas.validar_fecha_hora(fecha_i,prevenir_futuro=False)
            fecha_i = fecha_f - dt.timedelta(days=1)
        elif (fecha_i is not None) and (fecha_f is None):
            fecha_f = fechas.validar_fecha_hora(fecha_f,prevenir_futuro=False)
            fecha_f = fecha_i + dt.timedelta(days=1)
        else:
            #chequear que el orden sea correcto
            fecha_i = fechas.validar_fecha_hora(fecha_i,prevenir_futuro=False)
            fecha_f = fechas.validar_fecha_hora(fecha_f,prevenir_futuro=False)
        
        fecha_i = fecha_i.replace(microsecond=0)
        fecha_f = fecha_f.replace(microsecond=0)
        return f'(fecha >= "{fecha_i}") AND (fecha <= "{fecha_f}")'
            
    def __get_SQL_query(self, fecha_i=None, fecha_f=None, parques=[]):
        
        if fecha_i is None:
            fecha_i = self.fecha_i
        
        if fecha_f is None:
            fecha_f = self.fecha_f
            
        if isinstance(parques,(list,tuple,set)):
            #Chequear que todos los ítems sean strings
            all_strs = all(map(lambda x: isinstance(x,str),parques))
            if all_strs:
                parques = list(map(lambda x: x.upper(),parques))
            else:
                raise TypeError(f'Se esperaba que todos los parques sean del tipo string.')
        elif isinstance(parques,str):
            parques = [parques.upper(),]
        else:
            raise TypeError(f'Se esperaba que el parámetro parques sea del tipo list, tuple, set o string')
        
        # Si la lista de parques está vacía, no se debería tener que hacer nada
        if parques:
            idmedidores = ", ".join(str(x) for x in 
                self.medidores_smec
                   .loc[self.medidores_smec.Nemo.isin(parques), 'idcentral']
                   .unique()
                )
            sql_park_list = f'(idcentral IN ({idmedidores}))'
        else:
            sql_park_list = None
        
        sql_dates = self.__get_SQL_date_conditions(fecha_i=fecha_i,fecha_f=fecha_f)
        
        sql_query = 'SELECT * FROM crom.datos_smec WHERE '
        sql_query += ' AND '.join([x for x in [sql_park_list, sql_dates] if x is not None])
        return sql_query

    def __redondeo(self,numero):
        # Este es el tipo de redondeo que aplica CAMMESA (método antiguo)
        # Python redondea al número par más cercano.
        # Antiguamente se redondeaba al número siguiente si los decimales >= 0.5, si no hacia abajo

        n = abs(numero)
        entero =  int(n)
        decimal = n - entero

        return (entero if decimal < 0.5 else entero +1) * (-1 if numero < 0 else 1) 
    
    def consultar_datos_vc(self,fecha_i=None,fecha_f=None,parques=[],mensajes=False):
        if fecha_i is None:
            fecha_i = self.fecha_i
        
        if fecha_f is None:
            fecha_f = self.fecha_f
            
        if not parques and self.parques:
            parques = self.parques
        
        if self.checkear_conexion(mensajes=mensajes):
            self.datos_vc = (pd
                .read_sql(
                    self.__get_SQL_query(fecha_i=fecha_i, fecha_f=fecha_f, parques=parques),
                    self.conexion)
                .merge(
                    right=self.medidores_smec,
                    on = ['idcentral','idmedidor'],
                    how= 'left')
                .assign(
                    FechaOp = lambda df_: df_.fecha.apply(fechas.fecha_op),
                    E_Neta = lambda df_: df_.aportado.sub(df_.consumo).apply(self.__redondeo),
                    E_Neta_Gen = lambda df_: df_.E_Neta.mask(df_.E_Neta.le(0),0),
                    E_Neta_Con = lambda df_: df_.E_Neta.mask(df_.E_Neta.ge(0),0).mul(-1))
                .rename(columns = {'horaop':'HoraOp','fecha':'t_stamp','aportado':'Egen','consumo':'Econ','tension':'V'})
                .rename(columns = lambda x: x.replace('react_q','Q'))
                .drop(columns=['eneta','enetagen','enetacon','E_Neta'])
                .loc[:,['Nemo','UC','idcentral',
                        'Medidor','idmedidor','Tipo','Marca',
                        't_stamp','FechaOp','HoraOp',
                        'Egen','Econ','V',
                        'Q4','Q3','Q2','Q1',
                        'E_Neta_Gen','E_Neta_Con',
                        'rel_tv']]
                .sort_values(by=['Nemo','Tipo','Medidor','t_stamp'], ignore_index=True)
                )
            self.desconectar(mensajes=mensajes)
        else:
            raise Exception('Imposible conectarse a la Base de Datos del CROM')
        
    def __orden_columnas_medidor(self, df_):

        #Nuevos nombres de columnas
        cols_fecha = ['FechaOp','HoraOp']
        cols_resto_viejas = [c for c in df_.columns if c not in cols_fecha]
        cols_resto_nuevas = ['Egen', 'Econ', 'V','Q4', 'Q3', 'Q2', 'Q1']    #Columnas por defecto
    
        marca = self.medidores_smec.query(f'Medidor == "{df_.columns[0]}"').Marca
        if not marca.empty:
            if marca.iat[0] in ['ACTARIS SL7000','CIRCUTOR']:
                #Sobrescribir nuevas columnas, si el medidor es marca ACTARIS
                cols_resto_nuevas = ['Econ','Egen', 'V','Q4', 'Q1', 'Q2', 'Q3']
        
        return (df_
            .rename(columns=dict(zip(cols_resto_viejas, cols_resto_nuevas)))
            .loc[:,cols_fecha + cols_resto_nuevas])
        
    def leer_archivo_prn(self,archivo,mensajes=False):
        if mensajes: print(f'Cargando {archivo.name}')
        return (pd
            .read_csv(archivo, skiprows=1,index_col=False)
            .pipe(lambda df_: df_.set_axis(df_.columns.str.strip(),axis=1)) # Elimina espacios antes y después del nombre de cada columna
            .assign(
                Aux = lambda df_: df_.Time
                    .str.strip()
                    .str.split(' '), # Ends up with values in a list, per cell ['date','time']
                FechaOp = lambda df_: pd
                    .to_datetime(df_.Aux
                        .apply(lambda x: x[0] if len(x)==2 else pd.NA)
                        .ffill()
                        ),
                HoraOp = lambda df_: df_.Aux.apply(lambda x: x[-1]),
                FechaReloj = lambda df_: df_.FechaOp.dt.strftime('%Y-%m-%d'),
                HoraReloj = lambda df_: df_.HoraOp.str.replace('24:00','00:00'),
                SumarDia = lambda df_: df_.HoraOp
                    .eq('24:00')
                    .apply(lambda x: dt.timedelta(days=int(x))),
                t_stamp = lambda df_: pd
                    .to_datetime(df_.FechaReloj
                        .add(" ")
                        .add(df_.HoraReloj)
                        )
                    .add(df_.SumarDia),
                Medidor = lambda df_: df_.columns[1],
                Modif = archivo.stat().st_mtime #Fecha de modificación del archivo en formato UNIX Time
                )
            .assign(HoraOp = lambda df_: df_.HoraOp
                    .str.split(':')
                    .apply(lambda x: int(x[0]) + (x[-1] != '00'))
                )
            .drop(columns=['Time','SumarDia','Aux','FechaReloj','HoraReloj'])
            .set_index(['Medidor','t_stamp','Modif'])
            .pipe(self.__orden_columnas_medidor)
            .assign(
                E_Neta = lambda df_: df_.Egen.sub(df_.Econ).apply(self.__redondeo),
                E_Neta_Gen = lambda df_: df_.E_Neta.mask(df_.E_Neta.le(0),0),
                E_Neta_Con = lambda df_: df_.E_Neta.mask(df_.E_Neta.ge(0),0).mul(-1)
                )
            .drop(columns=['E_Neta'])
            )
    
    def cargar_datos_prn(self,ruta=None,mensajes=False,filtra_fechas=False):
        
        if ruta is None:
            ruta = dirs.check_dir(dirs.raiz + '\\' + '01 Input')
        
        self.datos_prn = (pd
            .concat(
                objs = [self.leer_archivo_prn(a, mensajes=mensajes) for a in dirs.filtra_archivos(ruta.iterdir(),'prn')],
                axis = 0)
            #Eliminar duplicados
            .reset_index()
            .sort_values(by=['Medidor','t_stamp','Modif'])
            .drop_duplicates(subset=['Medidor','t_stamp'], keep='last')
            .drop(columns=['Modif'])
            #Combinar y reordenar
            .merge(
                right=self.medidores_smec,
                on='Medidor',
                how='left')
            .loc[:,['Nemo','UC','idcentral',
                    'Medidor','idmedidor','Tipo','Marca',
                    't_stamp','FechaOp','HoraOp',
                    'Egen','Econ','V',
                    'Q4','Q3','Q2','Q1',
                    'E_Neta_Gen','E_Neta_Con',
                    'rel_tv']]
            .sort_values(by=['Nemo','Tipo','Medidor','t_stamp'], ignore_index=True)
            .pipe(lambda df_, filtro=filtra_fechas: 
                df_.query(
                    self.__get_SQL_date_conditions(self.fecha_i,self.fecha_f)
                            .replace('fecha','t_stamp')) 
                    if filtro else df_)
            )

