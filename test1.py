from app import Main
import aiohttp
import asyncio
import pprint

def check(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


async def main(values, N):
    while True:
        Main.__init__(Main)
        Main.treatment(Main, values)
        print(Main.to_monitor)
        await asyncio.sleep(N)

if __name__ == '__main__':
    Main.__init__(Main)
    print(Main.valute)
    i = 0
    values = []
    while i == 0:
        Bool = (input('Add currency? y/f\n')).upper()
        if Bool == 'Y':
            valute = ((input('Enter currency\nExample: usd\n')).upper())
            if valute in Main.valute:
                values.append(valute)
            else:
                print('Wrong currency')
        elif Bool == 'F':
            i = i + 1
            while i == 1:
                N = input('Updating currency data (period)\n')
                if check(N):
                    N = int(N)
                    i = i + 1
                else:
                    print('Wrond period')
        else:
            print('Wrong y/f')
loop = asyncio.get_event_loop()
loop.run_until_complete(main(values, N))
