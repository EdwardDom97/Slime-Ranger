#an example of a def draw game state by Yum from PygameDiscord with a draw card action/event inside of it.


def game():
    current_state = ""

    cards_drawn = 0

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # No check for current_state, so occurs regardless of state
        if menubutt_rect.collidepoint((mx, my)):
            print("Hey there is collision")
            if click:
                return  # Goes back to main menu, as it is the one that calls game

        # Only occurs in blank state
        if current_state == "":
            if spellbutt_rect.collidepoint((mx, my)):
                if click:
                    current_state = "drawing_card"

        # Only occurs when drawing card
        elif current_state == "drawing_card":
            if cards_drawn <= 1 and spellbutt_rect.collidepoint((mx, my)):
                if click:
                    cards_drawn += 1

        # Always draw the following
        screen.fill("lightgray")
        screen.blit(cardpanimg, cardpanimg_rect)
        screen.blit(player_image, player_rect)
        screen.blit(earthslime, earthslime_rect)
        screen.blit(ground, ground_rect)
        # want to add my 'draw' button 'menu' button and card(s).
        screen.blit(menubutton, menubutt_rect)
        screen.blit(drawspellbutton, spellbutt_rect)
        screen.blit(topcard, topcard_rect)

        # Only blits when "drawing_card"
        if current_state == "drawing_card":
            screen.blit(manashot, manashot_rect)

        pygame.display.update()
        clock.tick()  # You can just leave this blank, to tick as fast as possible
