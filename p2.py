"""
Práctica 2: Algoritmos codiciosos.
Algoritmia y Estructuras de Datos Avanzadas.
Curso 2026-27.
"""

from typing import List, Tuple, Dict, Optional
import random

# =============================================================================
# I. Problema del cambio de monedas
# =============================================================================

def greedy_change(coins: List[int], amount: int) -> Tuple[List[int], int]:
    """
    Estrategia codiciosa para el problema del cambio de monedas.
    Selecciona en cada paso la moneda de mayor valor que no supere la cantidad restante.
    """
    sorted_coins = sorted(coins, reverse=True)
    selected = []
    remainder = amount
    
    for coin in sorted_coins:
        while remainder >= coin:
            selected.append(coin)
            remainder -= coin
            
    return selected, remainder

def optimal_change(coins: List[int], amount: int) -> Optional[List[int]]:
    """
    Solución óptima mediante programación dinámica para el problema del cambio de monedas.
    Determina el menor número de monedas necesario para obtener la cantidad objetivo.
    """
    if amount == 0:
        return []
    if amount < 0 or not coins:
        return None

    # Ordenamos de mayor a menor sin modificar la lista de entrada
    sorted_coins = sorted(coins, reverse=True)
    
    # dp[i] almacenará la mejor lista de monedas (ordenada de mayor a menor) para la cantidad i
    dp: List[Optional[List[int]]] = [None] * (amount + 1)
    dp[0] = []

    for i in range(1, amount + 1):
        best_comb: Optional[List[int]] = None
        for coin in sorted_coins:
            if coin <= i and dp[i - coin] is not None:
                # Mantenemos la combinación ordenada de mayor a menor para comparar lexicográficamente
                candidate = sorted(dp[i - coin] + [coin], reverse=True)
                
                if best_comb is None:
                    best_comb = candidate
                elif len(candidate) < len(best_comb):
                    best_comb = candidate
                elif len(candidate) == len(best_comb) and candidate > best_comb:
                    best_comb = candidate
                    
        dp[i] = best_comb

    return dp[amount]


def compare_change(coins: List[int], max_amount: int) -> Dict[str, List[int]]:
    """
    Evalúa todas las cantidades entre 1 y max_amount, clasifica cada cantidad en
    'optimal', 'suboptimal', 'greedy_failed' o 'impossible'.
    """
    result: Dict[str, List[int]] = {
        "optimal": [],
        "suboptimal": [],
        "greedy_failed": [],
        "impossible": []
    }
    
    for amount in range(1, max_amount + 1):
        greedy_res, remainder = greedy_change(coins, amount)
        opt_res = optimal_change(coins, amount)
        
        if remainder != 0 and opt_res is None:
            result["impossible"].append(amount)
        elif remainder != 0 and opt_res is not None:
            result["greedy_failed"].append(amount)
        elif opt_res is not None:
            if len(greedy_res) == len(opt_res):
                result["optimal"].append(amount)
            else:
                result["suboptimal"].append(amount)
                
    return result

# =============================================================================
# II. Selección de actividades
# =============================================================================

def activity_selection(activities: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    """
    Selecciona el máximo número posible de actividades compatibles.
    Ordena por tiempo de finalización ascendente, y en caso de empate por inicio e identificador.
    """
    if not activities:
        return []
    
    sorted_activities = sorted(activities, key=lambda x: (x[2], x[1], x[0]))
    
    selected = [sorted_activities[0]]
    last_end = sorted_activities[0][2] 
    
    for act in sorted_activities[1:]:
        start = act[1]
        end = act[2]
        
        if start >= last_end:
            selected.append(act)
            last_end = end
            
    return selected

def generate_activities(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    """
    Genera n actividades aleatorias reproducibles.
    start en [0, 10000], duration en [1, 100], end = start + duration.
    """
    random.seed(seed)
    activities = []

    for i in range(n):
        start = random.randint(0, 10000)
        duration = random.randint(1, 100)
        end = start + duration
        activities.append((f"A{i}", start, end))
    
    return activities

# =============================================================================
# III. Planificación de tareas con fechas límite
# =============================================================================

def job_scheduling(jobs: List[Tuple[str, int, int]]) -> Tuple[List[Optional[Tuple[str, int, int]]], int]:
    """
    Planificación de tareas de duración unitaria con fecha límite (deadline).
    Devuelve la secuencia de tareas asignadas (con None para intervalos vacíos) y el beneficio total.
    """
    if not jobs:
        return [], 0
        
    sorted_jobs = sorted(jobs, key=lambda x: (-x[1], x[2], x[0]))

    max_deadline = max(job[2] for job in jobs)
    schedule = [None] * max_deadline
    total_profit = 0

    for job in sorted_jobs:
        job_id, profit, deadline = job
        
        for t in range(min(deadline, max_deadline) - 1, -1, -1):
            if schedule[t] is None:
                schedule[t] = job
                total_profit += profit
                break

    return schedule, total_profit

def generate_jobs(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    """
    Genera n tareas aleatorias con fecha límite reproducibles.
    profit en [1, 1000], deadline en [1, max(1, n // 10)].
    """
    random.seed(seed)
    jobs = []
    max_deadline = max(1, n // 10)

    for i in range(n):
        profit = random.randint(1, 1000)
        deadline = random.randint(1, max_deadline)
        jobs.append((f"J{i}", profit, deadline))

    return jobs
