number_of_completed_homeworke = 12
number_of_hours_spent = 1.5
course_name = 'Python'
time_for_one_task = number_of_hours_spent / number_of_completed_homeworke
print('Курс:',course_name,', Всего задач:', number_of_completed_homeworke,', затрачено часов:',
      number_of_hours_spent,', среднее время выполнения',time_for_one_task,'часа')
#  Запись с использованием f-строки позволяет упростить запись
print(f"Курс: {course_name}, Всего задач: {number_of_completed_homeworke}, затрачено часов: "
      f"{number_of_hours_spent}, среднее время выполнения {time_for_one_task} часа")
# Нам говорили, что можно использовать сторонний материал и я поискал его. Это полезно? Или выполнять задания только
# в рамках заданного материала?