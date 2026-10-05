from p1 import *
import matplotlib.pyplot as plt # Para imprimir gráficas. Entender código dado.


# Datos de ejemplo
n_list = [10, 50, 100, 250, 500, 1000]
    
print("Prueba de medicion has_sum_pair")

t = time_measure(has_sum_pair, dataprep_sum_pair_hit, n_list)
plot_single_curve(n_list, t)

t = time_measure(has_sum_pair, dataprep_sum_pair_miss, n_list)
plot_single_curve(n_list, t)

print("Prueba de medicion rle_encode")

t = time_measure(rle_encode_naive, dataprep_rle, n_list)
plot_single_curve(n_list, t)

t = time_measure(rle_encode_optimized, dataprep_rle, n_list)
plot_single_curve(n_list, t)