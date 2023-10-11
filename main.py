import os
from time import sleep

birthdays = []

def main():
  cont = ''
  while cont != 'n':
    question = input(
      'Would you like to save, find, or see your list of birthdays? (S/F/L): ').lower()
    if question == 's' or question == 'save':
      birthday = createBday()
      print('New birthday added:')
      print(
        f'Name: {birthday[0]}\nBirthday: {birthday[1]}/{birthday[2]}/{birthday[3]}\n'
      )
    if question == 'f' or question == 'find':
      birthdaysFound, count = findBday()
      print(f'\n{count} birthdays found:\n')
      for birthday in birthdaysFound:
        print(f'Name: {birthday[0]}\nBirthday: {birthday[1]}/{birthday[2]}/{birthday[3]}\n')
    if question == 'l' or question == 'list':
      listBday()
    cont = input("Continue? (Y/N): ").lower()
    if (cont == 'y'):
      print('clearing the screen...')
      sleep(1)
      os.system('clear')

def createBday():
  name = input("What is the name of the person whose birthday you would like to save? ").capitalize()
  month, day, year = askDate()
  newBirthday = [name, month, day, year]
  birthdays.append(newBirthday)
  return newBirthday

def findBday():
  find = input("Find by name or date? (N/D): ").lower()
  if find == 'n' or find == 'name':
    name = input('Name: ').lower()
    birthdays.sort(key=lambda row: row[0], reverse=False)
    birthdaysFound, count = findByName(name)
  if find == 'd' or find == 'date':
    month, day, year = askDate()
    birthdays.sort(key=lambda row: (row[3], row[1], row[2]), reverse=False)
    birthdaysFound, count = findByDate(month, day, year)
  for birthday in birthdaysFound:
    birthdays.append(birthday)
  return birthdaysFound, count

# binary search by name
def findByName(name):
  low = 0
  high = len(birthdays) - 1
  birthdaysFound = []
  count = 0
  while low <= high:
    mid = int((low + high) / 2)
    if birthdays[mid][0].lower() == name:
      count += 1
      birthdaysFound.append(birthdays[mid])
      birthdays.remove(birthdays[mid])
      high = len(birthdays) - 1
    else:
      if birthdays[mid][0].lower() < name:
        low = mid + 1
      if birthdays[mid][0].lower() > name:
        high = mid - 1
  return birthdaysFound, count

# binary search by date
def findByDate(month, day, year):
  low = 0
  high = len(birthdays) - 1
  birthdaysFound = []
  count = 0
  while low <= high:
    mid = int((low + high) / 2)
    if birthdays[mid][1] == month and birthdays[mid][2] == day and birthdays[mid][3] == year:
      count += 1
      birthdaysFound.append(birthdays[mid])
      birthdays.remove(birthdays[mid])
      high = len(birthdays) - 1
    else:
      if birthdays[mid][3] < year:
        low = mid + 1
      elif birthdays[mid][3] > year:
        high = mid - 1
      else:
        if birthdays[mid][1] < month:
          low = mid + 1
        elif birthdays[mid][1] > month:
          high = mid - 1
        else:
          if birthdays[mid][2] < day:
            low = mid + 1
          elif birthdays[mid][2] > day:
            high = mid - 1
  return birthdaysFound, count

# function to list all birthdays
def listBday():
  for birthday in birthdays:
    print(f'Name: {birthday[0]}\nBirthday: {birthday[1]}/{birthday[2]}/{birthday[3]}\n')

# function to ask for date and split it into the month day and year
def askDate():
  date = input("Date (MM/DD/YYYY): ").split('/')
  while len(date) != 3:
    date = input("Please follow the format MM/DD/YYYY: ").split('/')
  month = int(date[0])
  day = int(date[1])
  year = int(date[2])
  return month, day, year

main()
