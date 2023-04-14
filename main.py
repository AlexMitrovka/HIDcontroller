import time
from keyboard import Keyboard
from mouse import Mouse
from bot import Facade


keyboard = Keyboard()
mouse = Mouse()
facade = Facade(keyboard, mouse)
interval = float(0.1)
start_time = time.time()

""""""
text = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,\n" \
       " totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt \n" \
       "explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni \n" \
       "dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, c\n" \
       "onsectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat \n" \
       "voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid \n" \
       "ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae \n" \
       "consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
def main():
    with facade as b:
        for letter in text:
            b.kbWrite(letter)
            time.sleep(interval)

        # for i in range(1,21):
        #     b.kbPrint('Hello')
        #     b.move(199,100)
        #     b.move(500, 1000)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")


if __name__ == '__main__':
    main()