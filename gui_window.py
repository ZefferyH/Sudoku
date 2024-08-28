import pygame as p
import engine
import sys
#CONSTANTS

p.init()
BOARD_WIDTH = BOARD_HEIGHT = 720
FUNCTION_PANEL_HEIGHT = 240
FUNCTION_PANEL_WIDTH = BOARD_WIDTH
DIMENSION = 9
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 60
background_color = "white"
main_font = p.font.SysFont("Cambria Math",72, False, False)
player_font = p.font.SysFont("New Roman",72, False, False)
diff_select_font = p.font.SysFont("Cambria Math",46, False, False)
message_font = p.font.SysFont("Cambria Math",14, False, False)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
hover_blue = (0, 100, 255)
BUTTON_COLOR = "darkgrey"

def main():
    p.init()
    screen = p.display.set_mode((BOARD_WIDTH,+ BOARD_HEIGHT + FUNCTION_PANEL_HEIGHT))
    p.display.set_caption("Sudoku")
    clock = p.time.Clock()


    running = True
    square_selected = () #(row, col)
    State = engine.State()


    while running:
        mouse_location = p.mouse.get_pos()
        mouse_x = mouse_location[0]
        mouse_y = mouse_location[1]
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                ## Click Button
                # First Row
                if BOARD_HEIGHT <= mouse_y <= BOARD_HEIGHT + SQUARE_SIZE and square_selected != ():
                    button_clicked = mouse_x // SQUARE_SIZE + 1

                    if 1 <= button_clicked <= 9:
                        State.update(button_clicked,square_selected)
                # Second Row: Delete
                elif BOARD_HEIGHT + SQUARE_SIZE <= mouse_y <= BOARD_HEIGHT + 2 * SQUARE_SIZE:
                    if mouse_x <= SQUARE_SIZE * 2 and square_selected != ():
                        State.delete_number(square_selected[0], square_selected[1])
                        wipe_number(screen, square_selected[0], square_selected[1])
                # Second Row: Solve
                    elif mouse_x >= SQUARE_SIZE * 6:
                        square_selected = ()
                        graphics(screen, State, square_selected, -1)
                        State.solve_iteration = 0
                        if State.solve(screen) == False:
                            State.message = "No solution from current position"
                # Third Row: Difficulty Selection
                elif BOARD_HEIGHT + 2 * SQUARE_SIZE <= mouse_y <= BOARD_HEIGHT + 3 * SQUARE_SIZE:
                    if SQUARE_SIZE * 3 <= mouse_x <= SQUARE_SIZE * 5:
                        State.new_game("easy")
                    elif SQUARE_SIZE * 5 <= mouse_x <= SQUARE_SIZE * 7:
                        State.new_game("medium")
                    elif SQUARE_SIZE * 7 <= mouse_x <= SQUARE_SIZE * 9:
                        State.new_game("hard")
                # Select Board
                col = mouse_x // SQUARE_SIZE
                row = mouse_y // SQUARE_SIZE
                if square_selected == (row, col) or col > 8 or row > 8:
                    square_selected = ()
                else:
                    square_selected = (row, col)
            elif e.type == p.KEYDOWN:
                if square_selected != ():
                    if e.key == p.K_1:
                        State.update(1,square_selected)
                    elif e.key == p.K_2:
                        State.update(2,square_selected)
                    elif e.key == p.K_3:
                        State.update(3,square_selected)
                    elif e.key == p.K_4:
                        State.update(4,square_selected)
                    elif e.key == p.K_5:
                        State.update(5,square_selected)
                    elif e.key == p.K_6:
                        State.update(6,square_selected)
                    elif e.key == p.K_7:
                        State.update(7,square_selected)
                    elif e.key == p.K_8:
                        State.update(8,square_selected)
                    elif e.key == p.K_9:
                        State.update(9,square_selected)
                    elif e.key == p.K_DELETE:
                        State.delete_number(square_selected[0],square_selected[1])
                        wipe_number(screen, square_selected[0], square_selected[1])
                    square_selected = ()
                elif e.key == p.K_s:
                    square_selected = ()
                    graphics(screen,State,square_selected,-1)
                    State.solve_iteration = 0
                    if State.solve(screen) == False:
                        State.message = "No solution from current position"
                elif e.key == p.K_t: #test
                    pass

        ## Button Hover Effects
        # First Row
        if BOARD_HEIGHT <= mouse_y <= BOARD_HEIGHT + SQUARE_SIZE:
            hovered_button = mouse_x // SQUARE_SIZE

        # Second Row
        elif BOARD_HEIGHT + SQUARE_SIZE <= mouse_y <= BOARD_HEIGHT + 2 * SQUARE_SIZE:
            if mouse_x <= SQUARE_SIZE * 2:
                hovered_button = 10 # Delete
            elif mouse_x >= SQUARE_SIZE * 6:
                hovered_button = 11 # Solve
            else:
                hovered_button = -1
        # Third Row
        elif BOARD_HEIGHT + SQUARE_SIZE * 2 <= mouse_y <= BOARD_HEIGHT + 3 * SQUARE_SIZE:
            if SQUARE_SIZE * 3 <= mouse_x <= SQUARE_SIZE * 5:
                hovered_button = 12 # Easy
            elif SQUARE_SIZE * 5 <= mouse_x <= SQUARE_SIZE * 7:
                hovered_button = 13 # Medium
            elif SQUARE_SIZE * 7 <= mouse_x <= SQUARE_SIZE * 9:
                hovered_button = 14  # Hard
            else:
                hovered_button = -1
        else:
            hovered_button = -1
        if engine.find_empty(State.board) == False:
            State.message = "Solved!"
        graphics(screen,State,square_selected,hovered_button)

        p.display.flip()
        clock.tick(MAX_FPS)


    p.quit()
    sys.exit()

def graphics(screen,State,square_selected,hovered_button):
    screen.fill(p.Color(background_color))
    highlightSquares(screen, square_selected)
    draw_grid(screen)
    draw_numbers(screen, State)
    draw_buttons(screen,hovered_button)
    draw_delete_button(screen,hovered_button)
    draw_solve_button(screen,hovered_button)
    draw_diff_select_buttons(screen,hovered_button)
    draw_message(screen,State.message)

def draw_grid(screen):
    # 1x1
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            rect = p.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            p.draw.rect(screen, p.Color("black"), rect, 2)

    # 3x3
    for row in range(0, DIMENSION, 3):
        for col in range(0, DIMENSION, 3):
            rect = p.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, 3 * SQUARE_SIZE, 3 * SQUARE_SIZE)
            p.draw.rect(screen, p.Color("black"), rect, 4)



def draw_numbers(screen,State):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            number = State.board[row][col]
            if State.starting_position[row][col] != 0:
                number_object = main_font.render(str(number), 0, p.Color("Black"))
            else:
                number_object = main_font.render(str(number), 0, p.Color("#02237c"))
            if number != 0:
                screen.blit(number_object, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE - 5))
def draw_buttons(screen,button_number):
    for i in range(1,10):
        if button_number + 1 == i:
            button(screen,i,"#909090")
        else:
            button(screen,i,"#575757")
def button(screen,i,color):
    x = SQUARE_SIZE * (i - 1)
    y = 720
    width = SQUARE_SIZE
    height = SQUARE_SIZE
    p.draw.rect(screen,color,(x,y,width,height))
    text_surface = main_font.render(str(i),True,"white")
    screen.blit(text_surface,
                (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) - 5 // 2))
def draw_delete_button(screen,hovered_button): # 10th Button
    if hovered_button == 10:
        color = "#be543e"
    else:
        color = "#ff2c00"
    x = 0
    y = SQUARE_SIZE * 10
    width = SQUARE_SIZE * 2
    height = SQUARE_SIZE
    p.draw.rect(screen,color,(x,y,width,height))
    text_surface = main_font.render("DEL",True,"white")
    screen.blit(text_surface,
                (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) - 5 // 2))
def draw_solve_button(screen,hovered_button):
    if hovered_button == 11:
        color = "#4bff5e"
    else:
        color = "#00a412"
    x = SQUARE_SIZE * 6
    y = SQUARE_SIZE * 10
    width = SQUARE_SIZE * 3
    height = SQUARE_SIZE
    p.draw.rect(screen,color,(x,y,width,height))
    text_surface = main_font.render("SOLVE",True,"white")
    screen.blit(text_surface,
                (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) - 5 // 2))
def draw_diff_select_buttons(screen, hovered_button):
    difficulties = ("easy","medium","hard")

    x_text = SQUARE_SIZE * 0
    x_easy = SQUARE_SIZE * 3
    x_medium = SQUARE_SIZE * 5
    x_hard = SQUARE_SIZE * 7
    difficulties_sizes = (x_easy,x_medium,x_hard)
    y = SQUARE_SIZE * 11
    text_width = SQUARE_SIZE * 3
    button_width = SQUARE_SIZE * 2
    height = SQUARE_SIZE
    if hovered_button == 12:
        colors = ("#909090","#575757","#575757")
    elif hovered_button == 13:
        colors = ("#575757","#909090","#575757")
    elif hovered_button == 14:
        colors = ("#575757", "#575757",  "#909090")
    else:
        colors = ("#575757", "#575757",  "#575757")
    # Text block
    p.draw.rect(screen, "#575757", (x_text, y, text_width, height))
    text = diff_select_font.render("New Game:", True, "white")
    screen.blit(text,
                (x_text + (text_width - text.get_width()) // 2,
                 y + (height - text.get_height()) // 2))
    # Diff block
    for i in range(3):
        p.draw.rect(screen,colors[i],(difficulties_sizes[i],y,button_width,height))
        text_surface = diff_select_font.render(difficulties[i], True, "white")
        screen.blit(text_surface,
                    (difficulties_sizes[i] + (button_width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))
def draw_message(screen,text):
    color = "#000000"
    x = SQUARE_SIZE * 2
    y = SQUARE_SIZE * 10
    width = SQUARE_SIZE * 4
    height = SQUARE_SIZE
    p.draw.rect(screen, color, (x, y, width, height))
    text_surface = message_font.render(text, True, "white")
    screen.blit(text_surface,
                (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height())// 2))
def highlightSquares(screen, square_selected):
    if square_selected != ():
        row, col = square_selected
        s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
        s.set_alpha(75)  # transparency
        s.fill(p.Color("blue"))
        screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))


def wipe_number(screen,row,col):
    square_rect = p.Rect(col * SQUARE_SIZE+10, row * SQUARE_SIZE+10, SQUARE_SIZE-20, SQUARE_SIZE-20)
    p.draw.rect(screen, background_color, square_rect)





if __name__ == "__main__":
    main()
