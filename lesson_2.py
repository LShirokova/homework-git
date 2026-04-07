# Задача 2. Функциональная обработка данных в Pandas

import pandas as pd
import numpy as np

np.random.seed(42)

# Дан DataFrame с информацией о продажах:
data = {
  'product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'],
  'price': [100, 150, 100, 200, 150, 100, 200, 150],
  'quantity': np.random.randint(1, 10, size=8) # [7 4 8 5 7 3 7 8]
}
df = pd.DataFrame(data)

# 1. Используя map для Series, создайте новый столбец 'revenue', который будет равен price * quantity.
df['revenue'] = list(map(lambda a, b: a * b, df['price'], df['quantity']))

# 2. Сгруппируйте данные по продукту и вычислите общую выручку для каждого продукта.
revenue_by_product = df.groupby('product')['revenue'].sum()

print("Выручка по продуктам:")
print(revenue_by_product)

# 3. Используя apply с lambda-функцией, отфильтруйте строки, где количество проданных единиц (quantity) больше среднего значения quantity по всему DataFrame. Выведите получившийся DataFrame.
mean_quantity = df['quantity'].mean() # среднее quantity
print(f"Продажи с quantity > среднего ({mean_quantity}):")

filtered_df = df[df.apply(lambda x: x['quantity'] > mean_quantity, axis=1)]
print(filtered_df)