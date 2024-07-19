
def liczba_armstronga(n):

  suma = 0
  
  for i in str(n):
    suma += int(i)**len(str(n))
  if suma > 9:
    return suma == n


def main():
  x = int(input('Podaj górny zakres wyświetlania liczb armstronga (większy od 153) '))
  for i in range(1, x):
    if liczba_armstronga(i):
      print(i)
      if i == x:
        break

if __name__ == "__main__":
  main()



