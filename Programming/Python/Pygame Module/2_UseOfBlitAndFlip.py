# import the pygame module, so you can use it
import pygame, os 
os.chdir("./Images")

# define a main function
def main():
    
    # initialize the pygame module
    pygame.init()
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180))
    
    # load image (it is in same directory)
    image = pygame.image.load("happy64_64.png")
    
    # blit image to screen
    screen.blit(image, (50,50))
    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()
    
    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    
    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
