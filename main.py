from program_prefab import *
import pygame



#img
sprite_load = load_image_by_url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f6404c03-17ad-466e-8a0b-adda8cf2ad43/dicthpy-a99cf215-a040-430b-afc4-30cb50bdb9ce.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Y2NDA0YzAzLTE3YWQtNDY2ZS04YTBiLWFkZGE4Y2YyYWQ0M1wvZGljdGhweS1hOTljZjIxNS1hMDQwLTQzMGItYWZjNC0zMGNiNTBiZGI5Y2UucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6Hw7DeJ5QZtgmy6xO5VH5JJEJEsr0Pyo2o26Rz2xwSE")


book_load = load_image_by_url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/27d0760b-b1e4-46a5-a5c3-33078eb2156e/d1hunmd-86ee44f4-0b84-4a96-8540-932575806765.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI3ZDA3NjBiLWIxZTQtNDZhNS1hNWMzLTMzMDc4ZWIyMTU2ZVwvZDFodW5tZC04NmVlNDRmNC0wYjg0LTRhOTYtODU0MC05MzI1NzU4MDY3NjUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.-kd8bqFOQgWSYbVjVavscGfhW5Ly7yx7aVyAHFc_EfU")
sheikah_icon = load_image_by_url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f6404c03-17ad-466e-8a0b-adda8cf2ad43/didndvz-c5ab4fd5-87fd-4e20-8e43-9a0b16758f50.png/v1/fill/w_1280,h_1280/sheikah_symbol_2k_by_matzero78_didndvz-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcL2Y2NDA0YzAzLTE3YWQtNDY2ZS04YTBiLWFkZGE4Y2YyYWQ0M1wvZGlkbmR2ei1jNWFiNGZkNS04N2ZkLTRlMjAtOGU0My05YTBiMTY3NThmNTAucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.X7odMeJaxKyljEn9rtr9cmtxPEVs_VruXW0zgO9b6Nc", resize_bool=True,scale=0.05)
link_jus_spritesheet = load_image_by_url("https://www.spriters-resource.com/resources/sheets/16/17154.png?updated=1460954676")
link_jus_spritesheet.set_colorkey([255,255,255])


uno_card = load_image_by_url("https://i.pinimg.com/originals/4c/74/ac/4c74acd62d09880e2c819c14a1c3a40a.png",resize_bool=True,scale=0.1)
Rubik_cube = load_image_by_url("https://i.redd.it/7ddmx0dnd8c11.png",resize_bool=True,scale=0.1)

#character
dict_sprites = {'imgs':[],'max':0}
def return_list_sprites(sprite_load):
    listi = [return_spritesheet(sprite_load,[0,520,64,60]),return_spritesheet(sprite_load,[0,648,64,60]),return_spritesheet(sprite_load,[0,584,64,60]),return_spritesheet(sprite_load,[0,714,64,60])]
    dict_sprites['imgs'].append(listi)
    dict_sprites['max'] = encontrar_maximo_de_elementos(dict_sprites['imgs'])-1
    return listi
list_sprites = return_list_sprites(sprite_load)
return_list_sprites(load_image_by_url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f6404c03-17ad-466e-8a0b-adda8cf2ad43/dif08r1-992f62af-e453-48e2-996b-48fab9192cf3.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Y2NDA0YzAzLTE3YWQtNDY2ZS04YTBiLWFkZGE4Y2YyYWQ0M1wvZGlmMDhyMS05OTJmNjJhZi1lNDUzLTQ4ZTItOTk2Yi00OGZhYjkxOTJjZjMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6K2Y3-nm8RYnymjsVAGa7HrblOFpbb6F2-oHtAmWPRo"))
return_list_sprites(load_image_by_url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f6404c03-17ad-466e-8a0b-adda8cf2ad43/diezuku-4a087943-de5f-42d4-adb8-1c0a418794b2.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Y2NDA0YzAzLTE3YWQtNDY2ZS04YTBiLWFkZGE4Y2YyYWQ0M1wvZGllenVrdS00YTA4Nzk0My1kZTVmLTQyZDQtYWRiOC0xYzBhNDE4Nzk0YjIucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.N7I5PctzrxiigUwC0IOOFQM1eRqOrIuxV41lOfmuSx4"))



list_sprites_fighter = [return_spritesheet(link_jus_spritesheet,[149,109,29,30],cantidad_frame=4),
                return_spritesheet(link_jus_spritesheet,[149,109,29,30],cantidad_frame=4),
                return_spritesheet(link_jus_spritesheet,[149,109,29,30],cantidad_frame=4,list_bool_flip=[True,False]),
                return_spritesheet(link_jus_spritesheet,[149,109,29,30],cantidad_frame=4),
                
                return_spritesheet(link_jus_spritesheet,[138,157,36,30],cantidad_frame=4),
                return_spritesheet(link_jus_spritesheet,[138,157,36,30],cantidad_frame=4),
                return_spritesheet(link_jus_spritesheet,[138,157,36,30],list_bool_flip=[True,False],cantidad_frame=4),
                return_spritesheet(link_jus_spritesheet,[138,157,36,30],cantidad_frame=4),]
#shadows


#npcs
link = create_the_npcs(list_sprites,[0,0],1,[scale_screen[0]//2,scale_screen[1]//2],[0,0],1,1,max_num_change=8)
link_negative = create_the_npcs(list_sprites,[0,0],1,[800,500],[0,0],0.28,0,max_num_change=8)
link_jus = create_the_npcs(list_sprites_fighter,[0,0],1,[0,scale_screen[1]//2],[0,0],0.20,1,max_num_change=3)
link_jus_negative = create_the_npcs(list_sprites_fighter,[0,0],1,[900,scale_screen[1]//2],[0,0],0.20,0,max_num_change=3)
#vehicle

    
#info
def on_book_mouse(pos,pos_mouse,distance=100,scale_txt=22,color_txt=[255,255,255]):
    
    
    screen.blit(book_load,pos)
    if Hover(pos_mouse,[pos[0],pos[1],distance,distance]):

        string_blit('1 = character follow mouse pos',pos,scale_txt,color_txt,screen)
        string_blit('mouse_left = 1',[pos[0],pos[1]+scale_txt],scale_txt,color_txt,screen)
        string_blit('mouse_scroll = 2',[pos[0],pos[1]+scale_txt*2],scale_txt,color_txt,screen)
        string_blit('mouse_right = 3',[pos[0],pos[1]+scale_txt*3],scale_txt,color_txt,screen)
        string_blit('2 = build',[pos[0],pos[1]+scale_txt*4],scale_txt,color_txt,screen)
        
        
#index mode
mode = {'index':0,'modes':['top','2d','ray'],'num_round':0}
def change_mode(icon_rect=[0,600,50,50],scale_txt=22,color_txt=[255,255,255]):
    screen.blit(sheikah_icon,icon_rect)
    
    if Hover(pygame.mouse.get_pos(),icon_rect) == True:
        string_blit('surf',icon_rect,scale_txt,color_txt,screen)
        if pygame.mouse.get_pressed()[0] == True:
            mode['index'] = 0
        if pygame.mouse.get_pressed()[1] == True:
            mode['index'] = 1
        if pygame.mouse.get_pressed()[2] == True:
            mode['index'] = 2

       
#skins 
def change_skin(icon_rect=[1200,600,50,50],scale_txt=22,color_txt=[255,255,255]):
    screen.blit(uno_card,icon_rect)
    
    if Hover(pygame.mouse.get_pos(),icon_rect) == True:
        string_blit('           skin',icon_rect,scale_txt,color_txt,screen)
        if pygame.mouse.get_pressed()[0] == True:
            link['list_img'] = dict_sprites['imgs'][0]
        if pygame.mouse.get_pressed()[1] == True:
            link['list_img'] = dict_sprites['imgs'][1]
        if pygame.mouse.get_pressed()[2] == True:
            link['list_img'] = dict_sprites['imgs'][2]

#builds
builts_back = pygame.Surface(scale_screen,pygame.SRCALPHA)
builts_front = pygame.Surface(scale_screen,pygame.SRCALPHA)
builts_front_3rd = pygame.Surface(scale_screen,pygame.SRCALPHA)
builts_surfaces = [builts_back,builts_front,builts_front_3rd]
builts_list_coords = {'list':[[0,0]],'max':0,'index':0}

#cube
builts_cube= pygame.Surface([10,10])
builts_cube.fill([255,0,0])

def Build(surf=builts_back,icon_rect=[1200,0,50,50],scale_txt=22,color_txt=[255,255,255]):
    screen.blit(surf,[0,0])
    screen.blit(Rubik_cube,icon_rect)
    
    if Hover(pygame.mouse.get_pos(),icon_rect) == True:
        string_blit('           build',icon_rect,scale_txt,color_txt,screen)
        if pygame.mouse.get_pressed()[0] == True:
            builts_cube.fill([255,0,0])
        if pygame.mouse.get_pressed()[1] == True:
            builts_cube.fill([255,255,0])
        if pygame.mouse.get_pressed()[2] == True:
            builts_cube.fill([0,255,0])
    else:
        if pygame.mouse.get_pressed()[1] == False:
            screen.blit(builts_cube,pygame.mouse.get_pos())
        if pygame.mouse.get_pressed()[1] == True:
            builts_list_coords['list'].append(pygame.mouse.get_pos())
            builts_list_coords['max'] = encontrar_maximo_de_elementos(builts_list_coords['list'])
            surf.blit(builts_cube,pygame.mouse.get_pos())
        if pygame.mouse.get_pressed()[0] == True:
            if builts_list_coords['max'] > 0:
                builts_list_coords['index'] = clock(builts_list_coords['index'],builts_list_coords['max'],1)
                surf.blit(builts_cube,builts_list_coords['list'][builts_list_coords['index']])
        
        
        

#clima

dict_clima = {'num':0}
clima_iluminación = pygame.Surface(scale_screen)

#main

def mostrar_img(self):
    #bg
    screen.fill([128,128,128])
    Build(surf=builts_surfaces[mode['index']])
    #modes
    if mode['modes'][mode['index']] == 'top':
        
        #reor
        bool_move = pygame.mouse.get_pressed()[2]
        index_for_angle(link,pygame.mouse.get_pos())
        link['vel_move'] = IF(bool_move,True,3,0)
        link['vel_transition'] = IF(bool_move,True,0.20,0)
        link['number_change'][0] = IF(bool_move,True,link['number_change'][0],0)
        #gameplay
        
        Avatar(screen,link,False)
        #second surf
        screen.blit(builts_front,[0,0])
        #3rd surf
        screen.blit(builts_front_3rd,[0,0])
        
        
    #respanw
    if Hover(link['rect_list'][0],[0,0,scale_screen[0],scale_screen[1]]) == False:
        link['rect_list'][0][0] = num_follow(link['rect_list'][0][0],0,link['vel_move'])
        link['rect_list'][0][1] = num_follow(link['rect_list'][0][1],0,link['vel_move'])
    #tutorial
    #reverse card for change character
    dict_clima['num'] = clock(dict_clima['num'],250,0.05)
    clima_iluminación.set_alpha(dict_clima['num'])
    screen.blit(clima_iluminación,[0,0])

    change_skin()
    
    on_book_mouse([0,0],pygame.mouse.get_pos())
    change_mode()

p1 = player
p1.function_normal = mostrar_img
p1(screen)

