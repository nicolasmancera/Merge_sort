def mergeSort(lista):
	if len(lista) <= 1:
		return lista

	p = len(lista) / 2
	izq = mergeSort(lista[:p])
	der = mergeSort(lista[p:])

	r = []
	while len(izq) > 0 and len(der) > 0:
		if izq[0] > der[0]:	
			r.append(der.pop(0))
		else:
			r.append(izq.pop(0))

	if len(izq) > 0:
		r.extend(mergeSort(izq))
	else:
		r.extend(mergeSort(der))

	return r