import pygame, sys, random, button, shop

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 675

GREEN = (13, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 3, 3)
GRAY = (80, 80, 80)
WHITE = (255, 255, 255)


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
FPS = 60


class Horse(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, type, ran, group):
		super().__init__()
		self.has_boost = False
		self.type = type
		self.speed = ran
		self.animate_fps = .4
		self.sprites = []
		for i in range(7):
			image = pygame.image.load(f"./asset/character/horse{main_game.index + 1}/{self.type}/{i + 1}.png")
			scale = image.get_width() / image.get_height()
			image = pygame.transform.scale(image, (scale * 150, 150))
			self.sprites.append(image)
		
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.bottomleft = (pos_x, pos_y)
		self.positonx = pos_x
		self.group = group
	
	def update(self, bua):
		if self.rect.right == main_game.rect_bua.left:
			main_game.showbua = False
		
		if self.rect.right <= WINDOW_WIDTH:
			
			self.positonx += (self.speed) * bua + 1
			
			self.rect.x = (self.positonx)
			
			self.animate(self.animate_fps)
		else:
			
			for ngua in self.group.sprites():
				if ngua == self:
					continue
				if not ngua.has_boost:
					ngua.speed += 2
					ngua.has_boost = True
			# main_game.rank.append(self)
			if len(main_game.rank) >= 1:
				main_game.speed_map = main_game.stop_map
	
	def animate(self, fps):
		self.current_sprite += fps
		if self.current_sprite >= 6:
			self.current_sprite = 0
		self.image = self.sprites[int(self.current_sprite)]


def coin():
	screen = main_game.screen
	base_font = pygame.font.Font(None, 32)
	user_text = ''
	input_rect = pygame.Rect(200, 200, 140, 32)
	color = pygame.Color(135, 206, 250)
	color2 = pygame.Color(255, 127, 90)
	run = True
	active = False
	temp = ''
	coin = 100
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if input_rect.collidepoint(event.pos):
					active = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					user_text = user_text[:-1]
				else:
					temp = event.unicode
					if temp.isdigit() and int(user_text + temp) <= coin:
						user_text += temp
		
		if active == True:
			color = color2
		pygame.draw.rect(screen, color, input_rect, 2)
		
		text_surface = base_font.render(user_text, True, (20, 25, 255))
		
		screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
		input_rect.w = max(100, text_surface.get_width() + 10)
		pygame.display.flip()


class Game():
	def __init__(self):
		self.WINDOW_WIDTH = 1200
		self.WINDOW_HEIGHT = 675
		self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		# hinh anh background
		background = pygame.image.load('./asset/img/cloud.png')
		scale = background.get_width() / background.get_height()
		self.background = pygame.transform.scale(background, (scale * 1200, 700))
		img_bua = pygame.image.load(f"./asset/bua/bua.png")
		self.img_bua = pygame.transform.scale(img_bua, (100, 100))
		self.rect_bua = self.img_bua.get_rect()
		#ngua
		HORSE1 = [
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/1/4.png"), (100, 100)), "ten1_1"],
			# tự đổi tên chỗ đây
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/2/4.png"), (100, 100)), "ten1_2"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/3/4.png"), (100, 100)), "ten1_3"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/4/4.png"), (100, 100)), "ten1_4"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/5/4.png"), (100, 100)), "ten1_5"]
		]
		# set 2
		HORSE2 = [
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/1/4.png"), (100, 100)), "ten2_1"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/2/4.png"), (100, 100)), "ten2_2"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/3/4.png"), (100, 100)), "ten2_3"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/4/4.png"), (100, 100)), "ten2_4"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/5/4.png"), (100, 100)), "ten2_5"]
		]
		# set /
		HORSE3 = [
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/1/4.png"), (100, 100)), "ten3_1"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/2/4.png"), (100, 100)), "ten3_2"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/3/4.png"), (100, 100)), "ten3_3"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/4/4.png"), (100, 100)), "ten3_4"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/5/4.png"), (100, 100)), "ten3_5"]
		]
		HORSE4 = [
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/1/4.png"), (100, 100)), "ten4_1"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/2/4.png"), (100, 100)), "ten4_2"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/3/4.png"), (100, 100)), "ten4_3"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/4/4.png"), (100, 100)), "ten4_4"],
			[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/5/4.png"), (100, 100)), "ten4_5"]
		]
		
		self.HORSE = [HORSE1, HORSE2, HORSE3, HORSE4]
		# Bua
		self.showbua = True
		self.rank = []
		self.bua_x = []
		self.list_horse = []
		for i in range(0, 5):
			self.bua_x.append(random.randint(200, 800))
		# tien
		self.coin = 1000
		# loai ngua
		self.index = 0
		# loai map
		self.map = 0
		# chay map
		self.stop_map = 0
		self.speed_map = 2
		
		#
		self.menu_music = pygame.mixer.Sound("./asset/sound/music.mp3")
		self.menu_music.set_volume(.2)
	
	def load_bg(self):
		
		self.menu_music.play(-1)
		img1 = pygame.image.load('./asset/img/bg1.png')
		background = pygame.transform.scale(img1, (1200, 800))
		img2 = pygame.image.load('./asset/img/cloud.png')
		cloud = pygame.transform.scale(img2, (1200, 600))
		img_button_start = pygame.image.load('./asset/img/button_start.png')
		button_start = pygame.transform.scale(img_button_start, (200, 100))
		button_start = button.Button(610, 150, 1, button_start)
		img_button_setting = pygame.image.load('./asset/img/button_setting.png')
		button_setting = pygame.transform.scale(img_button_setting, (240, 90))
		button_setting = button.Button(607, 280, 1, button_setting)
		running = True
		cloud_x = 0
		
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					if button_start.rect.collidepoint(pos):
						self.option_horse()
					
					if button_setting.rect.collidepoint(pos):
						print('danh')
			
			self.screen.blit(cloud, (cloud_x, -50))
			self.screen.blit(cloud, (cloud_x + 1170, -50))
			
			cloud_x -= 1
			self.screen.blit(background, (0, -125))
			if cloud_x == -1170:
				cloud_x = 0
			button_start.draw(self.screen)
			button_setting.draw(self.screen)
			pygame.display.update()
	
	def option_horse(self):
		running = True
		RECT = pygame.transform.scale(pygame.image.load(r"asset/img/rect.png"), (120, 120))
		RECT_hover = pygame.transform.scale(pygame.image.load(r"asset/img/rect.png"), (120, 120))
		START_BTN = button.Button(610, 600, 0.3, pygame.image.load(r"asset/img/button_start.png"))
		
		# tự đổi map chỗ đây
		MAP = [
			pygame.transform.scale(pygame.image.load(r"asset/map/map1.png"), (400, 200)),  # MAP1
			pygame.transform.scale(pygame.image.load(r"asset/map/map2.png"), (400, 200)),  # MAP2
			pygame.transform.scale(pygame.image.load(r"asset/map/map3.png"), (400, 200))  # MAP3
		]
		# set 1
		# tự chọn con ngựa khác cũng đc
		
		
		button_go_back = button.Button(50, 50, 0.1, pygame.image.load(r"asset/button/go_back.png"))
		button_shop = button.Button(100, 600, 0.4, pygame.image.load(r"asset/img/shop.png"))
		
		BG_x = 0
		
		rect_x = 260
		rect_y = 200
		
		horse_btn = []
		
		for i in range(0, 5):
			temp = button.Button_Horse(rect_x + 60 + 10, rect_y + 60 + 10, 1, self.HORSE[self.index][i][0])
			horse_btn.append(temp)
			rect_x += 150
		
		#CLick variable
		has_click_horse = False
		
		user_text = f"{min(30, self.coin // 2)}"
		font = pygame.font.Font("./asset/img/SourceCodePro-Black.ttf", 24)
		coin_text = font.render(f'COIN: {self.coin}', True, YELLOW)
		coin_text_rect = coin_text.get_rect()
		coin_text_rect.topright = (WINDOW_WIDTH - 20, 20)
		
		bet_text = font.render(f' BET: {user_text}', True, YELLOW)
		
		bet_text_rect = bet_text.get_rect()
		bet_text_rect.left = .36 * WINDOW_WIDTH
		bet_text_rect.centery = .22 * WINDOW_HEIGHT
		
		text_box = pygame.Rect(1, 1, WINDOW_WIDTH // 3.5,
		                       WINDOW_HEIGHT // 12)
		text_box.centerx = WINDOW_WIDTH // 2
		text_box.centery = .22 * WINDOW_HEIGHT
		
		color = YELLOW
		active = False
		error = False
		
		while running:
			clock.tick(60)
			
			#error bet
			error = (len(user_text) >= 15) or (not user_text.isdigit()) or (int(user_text) <= 0) or (
					int(user_text) > self.coin)
			
			if active:
				if error:
					color = RED
				else:
					color = GREEN
			else:
				color = YELLOW
				
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				
				if event.type == pygame.KEYDOWN:
					if active:
						if event.key == pygame.K_BACKSPACE:
							user_text = user_text[0: -1]
						else:
							if len(user_text) <= 16 and event.unicode.isdigit():
								user_text += event.unicode
								
				
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					pos = pygame.mouse.get_pos()
					for i in range(5):
						if horse_btn[i].rect.collidepoint(pos):
							self.bet = i + 1
							horse_btn[i].click = True
							has_click_horse = True
							for horse in horse_btn:
								if horse != horse_btn[i]:
									horse.click = False
									
					# Check Click Box
					if text_box.collidepoint(pos):
						active = True
					else:
						active = False
						
					if button_go_back.rect.collidepoint(event.pos):
						running = False
					# right_map
					# shopping
					if button_shop.rect.collidepoint(event.pos):
						shop.shop()
					if pygame.Rect((829, 380), (130, 130)).collidepoint(event.pos):
						if self.map == 2:
							self.map = 0
						else:
							self.map += 1
					# left_map
					if pygame.Rect((330, 380), (130, 130)).collidepoint(event.pos):
						if self.map == 0:
							self.map = 2
						else:
							self.map -= 1
					# right_chose_hourse
					if pygame.Rect((1000, 182), (100, 100)).collidepoint(event.pos):
						if self.index == 3:
							self.index = 0
						else:
							self.index += 1
						for i, btn in enumerate(horse_btn):
							btn.image = self.HORSE[self.index][i][0]
						
					
					# left_chose_hourse
					if pygame.Rect((182, 190), (100, 100)).collidepoint(event.pos):
						if self.index == 0:
							self.index = 3
						else:
							self.index -= 1
						for i, btn in enumerate(horse_btn):
							btn.image = self.HORSE[self.index][i][0]
					
					if pygame.Rect((490, 580), (250, 100)).collidepoint(event.pos) and has_click_horse==True:
						# LẤY GIÁ TRỊ MAP VỚI 5 CON NGỰA VÀ TÊN 5 CON NGỰA ĐỂ HIỂN THỊ ĐƯỜNG ĐUA TƯƠNG ỨNG
						self.maingame()
			#
			
			rect_x = 260
			rect_y = 200
			
			
			
			self.screen.blit(pygame.transform.scale(pygame.image.load("./asset/img/cloud.png").convert(), (1200, 900)),
			                 (BG_x, 0))
			
			for i in range(0, 5):
				horse_btn[i].draw(self.screen)
				# tên 5 con ngựa
				self.screen.blit(
					pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 20).render(f'{self.HORSE[self.index][i][1]}',
					                                                                  True, (246, 142, 2)),
					(rect_x + 20, rect_y - 25))
				rect_x += 150
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'<', True, (246, 142, 2)),
				(182, 190))  # đổi màu nút left tại đây
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'>', True, (246, 142, 2)),
				(1000, 190))  # có thể đổi màu
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 50).render(f'TÙY CHỈNH CHẾ ĐỘ', True,
				                                                                  (246, 142, 2)),
				(370, 50))  # có thể đổi màu
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 130).render(f'<', True, (246, 142, 2)),
				(330, 350))  # có thể đổi màu
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 130).render(f'>', True, (246, 142, 2)),
				(829, 350))  # có thể đổi màu
			self.screen.blit(MAP[self.map], (420, 350))
			self.screen.blit(MAP[self.map], (420, 350))
			START_BTN.draw(self.screen)
			button_go_back.draw(self.screen)
			button_shop.draw(self.screen)
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 50).render(f'SHOP', True, (246, 142, 2)),
				(50, 450))
			
			#rerender
			bet_text = font.render(f' BET: {user_text}', True, YELLOW)
			coin_text = font.render(f'COIN: {self.coin}', True, YELLOW)
			
			# blit bet
			self.screen.blit(bet_text, bet_text_rect)
			self.screen.blit(coin_text, coin_text_rect)
			pygame.draw.rect(self.screen, color, text_box, 3)
			
			pygame.display.update()


# đặt cược

	def maingame(self):
		print(main_game.index)
		self.menu_music.stop()
		ran = random.randint(2, 100) / 100
		horse_group = pygame.sprite.Group()
		horse1 = Horse(0, 260 + 110 * 0, 0 + 1, ran, horse_group)
		horse_group.add(horse1)
		ran = random.randint(2, 100) / 100
		horse2 = Horse(0, 260 + 110 * 1, 1 + 1, ran, horse_group)
		horse_group.add(horse2)
		ran = random.randint(2, 100) / 100
		horse3 = Horse(0, 260 + 110 * 2, 2 + 1, ran, horse_group)
		horse_group.add(horse3)
		ran = random.randint(2, 100) / 100
		horse4 = Horse(0, 260 + 110 * 3, 3 + 1, ran, horse_group)
		horse_group.add(horse4)
		ran = random.randint(2, 100) / 100
		horse5 = Horse(0, 260 + 110 * 4, 4 + 1, ran, horse_group)
		horse_group.add(horse5)
		racing = True
		dem = 0
		horse_x = [0, 0, 0, 0, 0]
		hidden = [True, True, True, True, True]  # hidden của bùa
		active = [False, False, False, False, False]  # trạng thái kích hoạt bùa
		horse = [horse1, horse2, horse3, horse4, horse5]  # lấy ra 5 con ngụaư cho dễ gọi vòng for
		bua = [3, 0.5, 0, -200, 200, 900]
		# tăng tốc
		# giảm tốc
		# choáng
		# tốc biến ngược
		# tốc biến until
		# về đích
		bua_get = [1, 1, 1, 1, 1, 1]  # bùa tạm thời
		end_bua = [0, 0, 0, 0, 0, 0]  # đêm vòng lặp để kết thúc trạng thái bùa
		bua_input = [1, 1, 1, 1, 1, 1]  # bùa truyền con ngựa
		end_horse = [False, False, False, False, False]  # trạng thái về đích của ngựa
		while racing:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			image = pygame.image.load(f'./asset/map/map{self.map + 1}.png')
			scale = image.get_width() / image.get_height()
			image_map = pygame.transform.scale(image, (scale * 800, 675))
			self.screen.blit(self.background, (0, 0))
			self.speed_map -= 2
			self.screen.blit(image_map, (self.speed_map, 0))
			self.screen.blit(image_map, (self.speed_map + 600, 0))
			self.screen.blit(image_map, (self.speed_map + 600 * 2, 0))
			if self.speed_map == -600:
				self.speed_map = 0
			# =========
			for index, horse in enumerate(horse_group.sprites()):
				horse.update(bua_input[index])
				horse_x[index] = horse.positonx
			
			'''horses1.update(bua_input[0])
			horse_x[0] = horse1.positonx
			horses2.update(bua_input[1])
			horse_x[1] = horse2.positonx
			horses3.update(bua_input[2])
			horse_x[2] = horse3.positonx
			horses4.update(bua_input[3])
			horse_x[3] = horse4.positonx
			horses5.update(bua_input[4])
			horse_x[4] = horse5.positonx'''
			
			for i in range(5):
				# kích hoạt bùa và ẩn hình ảnh bùa
				if (horse_x[i] + 50) >= self.bua_x[i] and hidden[i]:
					hidden[i] = False
					active[i] = True
					bua_get[i] = random.randint(0, 5)  # random  bùa nhận được
			for i in range(5):
				if active[i] and int(end_bua[i]) <= 160:  # kiểm tra điều kiện kích hoạt bùa
					if 3 <= bua_get[i] <= 4:
						horse_group.sprites()[i].positonx += bua[bua_get[i]]
						end_bua[i] = 170
					elif bua_get[i] == 5:
						horse_group.sprites()[i].positonx = bua[bua_get[i]]
						end_bua[i] = 170
					else:
						bua_input[i] = bua[bua_get[i]]
						end_bua[i] += 1
				elif end_bua[i] > 20:
					bua_input[i] = 1
				if horse_group.sprites()[i].rect.right >= WINDOW_WIDTH and (not end_horse[i]):
					self.rank.append(i)
					end_horse[i] = True
					print(self.rank)
			if len(self.rank) == 5:
				self.end()
			# =============
			horse_group.draw(self.screen)
			for i in range(1, 6):
				if self.showbua and hidden[i - 1]:
					self.screen.blit(self.img_bua, (self.bua_x[i - 1], 40 + i * 105))
			pygame.display.flip()
			clock.tick(60)
	def end(self):
		ending=True
		while ending:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			self.screen.blit(pygame.transform.scale(self.background,(1200,800)),(0,0))
			# hạng 1
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'1: ', True, BLACK),
				(50, 50))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[0]+1}/1.png"),(100,100)), (200,50))
			#hạng 2
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'2: ', True, BLACK),
				(50, 150))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[1]+1}/1.png"),(100,100)), (200,150))
			#hạng 3
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'3: ', True, BLACK),
				(50, 250))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[2]+1}/1.png"),(100,100)), (200,250))
			#hạng 4
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'4: ', True, BLACK),
				(50, 350))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[3]+1}/1.png"),(100,100)), (200,350))
			#hạng 5
			self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 100).render(f'5: ', True, BLACK),
				(50, 450))
			self.screen.blit(pygame.transform.scale(pygame.image.load(f"./asset/character/horse{self.index+1}/{self.rank[4]+1}/1.png"),(100,100)), (200,450))

			if self.bet==self.rank[0]+1:
				self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 50).render(f'YOU WON', True, BLACK),
				(100, 450))
			else: self.screen.blit(
				pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf', 50).render(f'DEFEAT', True, BLACK),
				(450, 100))
			pygame.display.update()


pygame.init()
main_game = Game()
main_game.load_bg()
pygame.quit()

