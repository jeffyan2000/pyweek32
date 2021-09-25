from config import *

class ChatScene:
    def __init__(self, chat_name, next_map=False):
        self.conversation = []
        self.next_map = next_map
        for sentence in chats[chat_name]:
            self.conversation.append(sentence)
        self.current_lines = []
        self.current_name = ""
        self.current_texture = "me_chat"
        self.next_dialog()
        self.dead = False

    def next_dialog(self):
        if self.conversation:
            next_c = self.conversation.pop(0)
            self.current_lines = []
            self.current_texture = next_c[2]
            self.current_name = font_chat_name.render(next_c[0], True, (0, 0, 0))
            current_line = ""
            sentence = next_c[1].split()
            for word in sentence:
                current_line += " " + word
                if font_chat_content.size(current_line)[0] > 650:
                    self.current_lines.append(current_line[:(-len(word))].strip())
                    current_line = word
            if current_line:
                self.current_lines.append(current_line.strip())
            for i in range(len(self.current_lines)):
                self.current_lines[i] = font_chat_content.render(self.current_lines[i], True, (0, 0, 0))
        else:
            self.dead = True

    def draw(self):
        pos = (- (ENV["mouse_x"] - SCREEN_WIDTH / 2) * (100 / 700) ** 2,
               - (ENV["mouse_y"] - SCREEN_HEIGHT / 2) * (100 / 700) ** 2)
        screen.blit(texture_lib[self.current_texture], pos)
        screen.blit(texture_lib["chat_box"], (0, 0))
        screen.blit(self.current_name, (95, 265))
        for i in range(len(self.current_lines)):
            screen.blit(self.current_lines[i], (75 - pos[0], 310 + i*25 - pos[1]))

class NextScene:
    def __init__(self, line, reverse=False):
        self.line = line
        self.reverse = reverse
        if not self.reverse:
            self.text1 = font_next_day.render(self.line, True, (255, 255, 255))
            self.text2 = font_next_day.render(self.line, True, (200, 200, 200))
            self.text3 = font_next_day.render(self.line, True, (150, 150, 150))
            self.text4 = font_next_day.render(self.line, True, (100, 100, 100))
        else:
            self.text1 = font_next_day.render(self.line, True, (0, 0, 0))
            self.text2 = font_next_day.render(self.line, True, (55, 55, 55))
            self.text3 = font_next_day.render(self.line, True, (105, 105, 105))
            self.text4 = font_next_day.render(self.line, True, (155, 155, 155))
        self.circle_radius = 0
        self.display_countdown = 90
        self.pos = 0
        if self.reverse:
            self.pos += 20
        self.dead = False

    def draw(self):
        if self.reverse:
            bg = (255, 255, 255)
        else:
            bg = (0, 0, 0)
        if self.circle_radius < 500 and self.display_countdown > 0:
            self.circle_radius += 20
            screen.fill(bg)
        elif self.circle_radius > 0 and self.display_countdown <= 0:
            self.circle_radius -= 20
            pygame.draw.circle(screen, bg, (400, 250), self.circle_radius)
        elif self.display_countdown >= 1:
            self.display_countdown -= 1
            screen.fill(bg)
            if not self.reverse and self.pos+6 < len(q_s):
                screen.blit(self.text4, (q_s[self.pos], 220))
                screen.blit(self.text3, (q_s[self.pos+2], 220))
                screen.blit(self.text2, (q_s[self.pos+4], 220))
                screen.blit(self.text1, (q_s[self.pos+6], 220))
                self.pos += 1
            elif self.reverse:
                p = len(q_s) - self.pos
                if p < 0:
                    p = 0
                screen.blit(self.text4, (q_s[p], 220))
                p = len(q_s) - self.pos - 2
                if p < 0:
                    p = 0
                screen.blit(self.text3, (q_s[p], 220))
                p = len(q_s) - self.pos - 4
                if p < 0:
                    p = 0
                screen.blit(self.text2, (q_s[p], 220))
                p = len(q_s) - self.pos - 6
                if p < 0:
                    p = 0
                screen.blit(self.text1, (q_s[p], 220))
                self.pos += 1
        else:
            self.dead = True

class EndScene:
    def __init__(self):
        self.dead = False
        self.close = 0
        self.cycle = Cycle(8, 2)

    def draw(self):
        screen.fill(0, pygame.Rect(0, 0, 800, self.close))
        screen.fill(-1, pygame.Rect(0, 500-self.close, 800, self.close))
        if self.close < 250:
            self.close += 3
        else:
            screen.blit(texture_lib["thank_you"], (0, 0))
            screen.blit(texture_lib["spin" + str(self.cycle.get()+1)], (200, 0))



chats = {
    "start": (
        ("me", "yawnnnnnnnnnn",
         "me_chat"),
        ("me", "why is my head hurting for no reason",
         "me_chat"),
        ("me", "what's the noise coming from living room?",
         "me_chat")),
    "door": (
        ("???", "did you make yourself drunk again?",
         "door_chat"),
        ("???", "it's no---ne of your busi--ness",
         "door_chat"),
        ("???", "*smack*",
         "door_chat"),
        ("???", "AH-",
         "door_chat")),
    "day1": (
        ("mom", "*sob*",
         "mom_chat"),
        ("dad", "what do y--ou mean by ag--ain",
         "dad_chat"),
        ("dad", "I **** do what---ever I want",
         "dad_chat"),
        ),
    "mom": (
        ("mom", "honey you should go take a walk on the street",
         "mom_chat"),
        ("mom", "take this money and buy some snacks",
         "mom_chat")),
    "day1street": (
        ("me", "mom and dad are arguing again...",
         "me_chat"),
        ("me", "mom always gets hurt, I want this to stop. but what can I do?",
         "me_chat")),
    "mystery": (
        ("mystery", "hello little girl, you look sad",
         "mystery_chat"),
        ("me", "my dad and mom are fighting again, they always do that, what should I do?",
         "me_chat"),
        ("mystery", "if they are hurting each other, there is one thing you can do",
         "mystery_chat"),
        ("mystery", "I'll sell you this box for a day of your life, it can solve your problem",
         "mystery_chat"),
        ("me", "what does the box do?",
         "me_chat"),
        ("mystery", "touch the box at night, and you will find out",
         "mystery_chat"),
        ("me", "ok...? I guess I can give it a try",
         "me_chat"),
        ("mystery", "...heheh",
         "mystery_chat"),
    ),
    "day1night": (
        ("me", "it's night time already...",
         "me_chat"),
        ("me", "maybe it's time to tryout that box thingy",
         "me_chat")),
    "box": (
        ("me", "Here we go",
         "me_chat"),
        ("me", "WOA-",
         "me_chat")),
    "p1": (
        ("me", "where, where am I?",
         "me_chat"),
        ("me", "the calendar over there says.. it's year 2000?",
         "me_chat"),
        ("me", "wait, I remember this restaurant! mom told me that this is where they met and started dating each other",
         "me_chat"),
        ("me", "if I do something to prevent them from dating... they won't marry each other!",
         "me_chat"),
        ("me", "there's the table they are going to sit at, maybe I can do something with it",
         "me_chat"),
    ),
    "medicine": (
        ("me", "that looks like a laxative, maybe someone was having trouble poo poo",
         "me_chat"),
    ),
    "table1": (
        ("me", "there a cup of water, I wonder if I can add some things in there",
         "me_chat"),
    ),
    "table2": (
        ("me", "let me put this medicine in there...",
         "me_chat"),
        ("me", "there we go! let's see what's going to happen",
         "me_chat"),
    ),
    "p1r": (
        ("dad", "...you should try the daily special steak dinner *sip*",
         "dad_chat"),
        ("mom", "that sounds great, we should also order the shrimps-",
         "mom_chat"),
        ("dad", "-AH, my stomach is aching all of a sudden, would you excuse me for a minute?",
         "dad_chat"),
        ("mom", "I'll wait for you here",
         "mom_chat"),
        ("me", "hehe looks like it worked, but it's probably not enough to stop them from dating each other",
         "me_chat"),
        ("me", "I remember that they went to a park on the next day, I should head over there before them",
         "me_chat"),
    ),
    "p2": (
        ("me", "this is the park in the photo!",
         "me_chat"),
        ("me", "and that's the path they are going to take",
         "me_chat"),
        ("me", "I wonder if I can do something with it",
         "me_chat"),
    ),
    "shovel": (
        ("me", "the gardener probably left the shovel here",
         "me_chat"),
    ),
    "hole1": (
        ("me", "this part of ground feels soft",
         "me_chat"),
        ("me", "maybe I can dig a hole here",
         "me_chat"),
    ),
    "hole2": (
        ("me", "huff huff",
         "me_chat"),
        ("me", "there we go! the hole is done",
         "me_chat"),
        ("me", "let's wait for them to walk pass here",
         "me_chat"),
    ),
    "p2r": (
        ("dad", "...the weather is so nice today, I wish this season was longer",
         "dad_chat"),
        ("mom", "I know right, the sky is so clear and the cloud is fluffy",
         "mom_chat"),
        ("dad", "oh, about the hotel we arranged toni-",
         "dad_chat"),
        ("dad", "AH",
         "dad_chat"),
        ("mom", "are you alright? Ew why is there a poop hole here",
         "mom_chat"),
        ("dad", "It's so disgusting, let's head to the hotel so I can take a shower asap",
         "dad_chat"),
        ("me", "that's strange, I don't recall putting poop in the hole",
         "me_chat"),
        ("me", "but anyways, they are heading to the hotel now, I'm one step away from preventing the marriage!",
         "me_chat"),
    ),
    "p3": (
        ("me", "this should be the room they are staying, luckily the door was unlocked!",
         "me_chat"),
        ("me", "let's see what can we do here",
         "me_chat"),
    ),
    "cream1": (
        ("me", "dad is probably going to use this cream when showering",
         "me_chat"),
    ),
    "cream2": (
        ("me", "there's a small opening, I should be able to inject it in there",
         "me_chat"),
        ("me", "done!",
         "me_chat"),
        ("me", "wait, what's happening?",
         "me_chat2"),
        ("me", "I'm.. disappearing",
         "me_chat2"),
        ("me", "why?",
         "me_chat2"),
        ("mystery", "because your parents never married each other, and therefore you don't exist anymore",
         "mystery_chat"),
        ("me", "wh&t $ow c@% I s@v% m!self?",
         "me_chat2"),
        ("mystery", "travel back in time and save this marriage, it's the only way to save yourself",
         "mystery_chat"),
        ("mystery", "stand tight...",
         "mystery_chat"),
        ("me", "wh@-",
         "me_chat2"),
    ),
    "injector": (
        ("me", "this looks like a needle... ew it smells",
         "me_chat"),
        ("me", "who left it here? why is it on the ground?",
         "me_chat"),
        ("me", "but anyways... this will be useful",
         "me_chat"),
    ),
    "q1": (
        ("me", "to save myself I need to undo my traps...",
         "me_chat"),
        ("me", "we should start off getting rid of the medicine",
         "me_chat"),
    ),
    "q12": (
        ("me", "there's no time to clean the cup",
         "me_chat"),
        ("me", "I can't make a scene either, I shouldn't let people notice me",
         "me_chat"),
        ("me", "I'll just dilute it",
         "me_chat"),
    ),
    "q2": (
        ("me", "there's the hole I dug, I need to cover it",
         "me_chat"),
    ),
    "q22": (
        ("me", "luckily I kept the shovel",
         "me_chat"),
        ("me", "ew a dog pooped in there, I don't have time to clean that, I'll just dig the hole",
         "me_chat"),
        ("me", "phew, the hole is filled, but it's still a little soft though",
         "me_chat"),
        ("me", "I'll just toss the shovel there, it's too heavy",
         "me_chat"),
    ),
    "q3": (
        ("me", "finally it's the face cream...",
         "me_chat"),
    ),
    "q32": (
        ("me", "I'll just suck it out using the injector",
         "me_chat"),
        ("me", "there we go, I'm not disappearing! it worked!",
         "me_chat"),
        ("me", "that means I probably can't stop them from marrying each other...",
         "me_chat"),
        ("mystery", "are you ready to head back?", "mystery_chat"),
        ("me", "yea... I guess there is nothing I can do in the past",
         "me_chat"),
        ("mystery", "oh you also need to leave the injector here", "mystery_chat"),
        ("me", "alright, I'll just put it here",
         "me_chat"),
        ("mystery", "alright, hold tight", "mystery_chat"),
        ("mystery", "by the way you will lose all of your memories when you go back", "mystery_chat"),
        ("me", "excuse m-", "me_chat"),
    ),
}