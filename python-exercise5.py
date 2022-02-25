def analisis():
    import csv
    path = "data.csv"
    ciudad = input()
    listado_precipitacion=[]
    listado_profundidad=[]
    listado_aptitud=[]
    impresion_uno=[]
    impresion_max=[]
    impresion_min=[]
    suma_precipitacion= 0
    suma_profundidad= 0
    aptitud_valor=[]
    aptitud_codigo=['sumamente apto','moderadamente apto','marginalmente apto','no apto']
             
    with open(path) as f:
        data = f.readlines()
        for linea in data:
            vals = linea.split(',')
            if vals[0] == ciudad:
                precipitacion = vals [4]
                precipitacion =int(precipitacion)
                listado_precipitacion.append(precipitacion)
                profundidad = vals [5]
                profundidad = int(profundidad)
                listado_profundidad.append(profundidad)
                aptitud = vals[6]
                aptitud = aptitud.replace("\n","")
                listado_aptitud.append(aptitud)
    for i in range (0, (len(listado_precipitacion))):
        valor_precipitacion = float(listado_precipitacion[i])
        suma_precipitacion = suma_precipitacion + valor_precipitacion
    promedio_precipitacion = round((suma_precipitacion / (len(listado_precipitacion))),2)
    impresion_uno.append("{:.2f}".format(promedio_precipitacion))
    for i in range (0, (len(listado_profundidad))):
        valor_profundidad = float(listado_profundidad[i])
        suma_profundidad = suma_profundidad + valor_profundidad
    promedio_profundidad = round((suma_profundidad / (len(listado_profundidad))),2)
    impresion_uno.append("{:.2f}".format(promedio_profundidad))
    print(*impresion_uno)
    
    minimo_precipitacion = min(listado_precipitacion)
    impresion_min.append(minimo_precipitacion)
    minimo_profundidad = min(listado_profundidad)
    impresion_min.append(minimo_profundidad)
    print(*impresion_min)
    
    maximo_precipitacion = max(listado_precipitacion)
    impresion_max.append(maximo_precipitacion)
    maximo_profundidad = max(listado_profundidad)
    impresion_max.append(maximo_profundidad)
    print(*impresion_max)
    sumamente=(listado_aptitud.count("sumamente apto"))
    moderadamente=(listado_aptitud.count("moderadamente apto"))
    marginalmente=(listado_aptitud.count("marginalmente apto"))
    noapto=(listado_aptitud.count("no apto"))
    
    aptitud_valor.append(sumamente)
    aptitud_valor.append(moderadamente)
    aptitud_valor.append(marginalmente)
    aptitud_valor.append(noapto)
    aptitud_final = list(zip(aptitud_codigo, aptitud_valor))
    aptitud_final = sorted(aptitud_final, key=lambda valor : valor[1], reverse=True)
    aptitud_final = sorted(aptitud_final, key=lambda codigo : codigo[0])
    
    for i,j in aptitud_final:
        print(str(i) + ' ' + str(j))
if __name__ == '__main__':
    analisis()
