import pygame
import math
import importlib
import app_0
import app_1
import app_2
import app_3
import app_4
import app_5
import app_6
import app_7
import app_8
import app_9
import app_10
import app_11
import app_12
import app_13
import app_14
import app_15
import app_16
import app_17
import app_18
import app_19
import app_20
import app_21
import app_22
import app_23

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1512, 900
BG_COLOR = (0, 0, 0)
CIRCLE_COLOR = (20, 20, 40)
OUTLINE_COLOR = (173, 216, 230)
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 18)

# Circle properties
CENTER = (WIDTH // 2, HEIGHT // 2)
CENTER_RADIUS = 100
SURROUND_RADIUS = 50
SURROUND_DISTANCE = 160
NEW_CIRCLE_RADIUS = 30
NEW_CIRCLE_DISTANCE = 80
# Image paths
logo_path = '/Users/mac6ssev/Desktop/MAT/pics/SSEVSOFTSOLS logo.png'

second_layer_images = [
    "/Users/mac6ssev/Downloads/circular_icons/icon_1.png", "/Users/mac6ssev/Downloads/circular_icons/icon_2.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_3.png", "/Users/mac6ssev/Downloads/circular_icons/icon_4.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_5.png", "/Users/mac6ssev/Downloads/circular_icons/icon_6.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_7.png", "/Users/mac6ssev/Downloads/circular_icons/icon_8.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_9.png", "/Users/mac6ssev/Downloads/circular_icons/icon_10.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_11.png", "/Users/mac6ssev/Downloads/circular_icons/icon_12.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_13.png", "/Users/mac6ssev/Downloads/circular_icons/icon_14.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_15.png", "/Users/mac6ssev/Downloads/circular_icons/icon_16.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_17.png", "/Users/mac6ssev/Downloads/circular_icons/icon_18.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_19.png", "/Users/mac6ssev/Downloads/circular_icons/icon_20.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_21.png", "/Users/mac6ssev/Downloads/circular_icons/icon_22.png",
    "/Users/mac6ssev/Downloads/circular_icons/icon_23.png", "/Users/mac6ssev/Downloads/circular_icons/icon_24.png"
]
# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circular UI")

# Load and resize logo
logo_img = pygame.image.load(logo_path).convert_alpha()
logo_img = pygame.transform.smoothscale(logo_img, (CENTER_RADIUS * 2, CENTER_RADIUS * 2))

# Create a circular mask
mask_surface = pygame.Surface((CENTER_RADIUS * 2, CENTER_RADIUS * 2), pygame.SRCALPHA)
pygame.draw.circle(mask_surface, (255, 255, 255, 255), (CENTER_RADIUS, CENTER_RADIUS), CENTER_RADIUS)

# Apply mask to logo
masked_logo = logo_img.copy()
masked_logo.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

# Load second-layer images
icon_images = []
for path in second_layer_images:
    try:
        img = pygame.image.load(path).convert_alpha()  # Convert to 32-bit with alpha
        img = pygame.transform.smoothscale(img, (NEW_CIRCLE_RADIUS * 2, NEW_CIRCLE_RADIUS * 2))
        icon_images.append(img)
    except pygame.error as e:
        print(f"Error loading image {path}: {e}")
        icon_images.append(None)  # Placeholder for missing images



# Define text labels
labels = [
    "CAD", "MEASURE", "ARCADE", "CALENDAR",
    "SOCIAL MEDIA", "INTERNET", "SETTINGS", "FILE EXPLORER"
]

angles = [i * (math.pi / 4) for i in range(8)]
frames = 30
step = 1 / frames
clock = pygame.time.Clock()

# Animation states
expanded = False
animating = False
surrounding_states = [{"progress": 0} for _ in labels]
new_circle_states = [{"progress": 0} for _ in range(24)]
active_index = None  # Keeps track of the currently expanded main circle


#launch app
def launch_app(index):
    try:
        module_name = f"app_{index}"
        app_module = importlib.import_module(module_name)
        app_module.launch()
    except ModuleNotFoundError:
        print(f"Module {module_name} not found!")


running = True
while running:
    screen.fill(BG_COLOR)

    if animating:
        for state in surrounding_states:
            state["progress"] = min(state["progress"] + step, 1) if expanded else max(state["progress"] - step, 0)

    for i, label in enumerate(labels):
        angle = angles[i]
        anim_distance = surrounding_states[i]["progress"] * SURROUND_DISTANCE
        x = CENTER[0] + anim_distance * math.cos(angle)
        y = CENTER[1] + anim_distance * math.sin(angle)
        
        pygame.draw.circle(screen, CIRCLE_COLOR, (int(x), int(y)), SURROUND_RADIUS)
        pygame.draw.circle(screen, OUTLINE_COLOR, (int(x), int(y)), SURROUND_RADIUS, 2)
        text_surface = FONT.render(label, True, TEXT_COLOR)
        screen.blit(text_surface, text_surface.get_rect(center=(int(x), int(y))))

        if i == active_index:
            for j in range(3):
                outer_index = i * 3 + j  # Unique index for subcircles (0-23)
                new_anim_distance = new_circle_states[outer_index]["progress"] * NEW_CIRCLE_DISTANCE
                new_angle = angle + (j - 1) * (math.pi / 4)  # Adjusted angles
                new_x = x + new_anim_distance * math.cos(new_angle)
                new_y = y + new_anim_distance * math.sin(new_angle)
                
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(new_x), int(new_y)), NEW_CIRCLE_RADIUS)
                pygame.draw.circle(screen, OUTLINE_COLOR, (int(new_x), int(new_y)), NEW_CIRCLE_RADIUS, 2)
                icon_index = i * 3 + j
                if 0 <= icon_index < len(icon_images) and icon_images[icon_index]:
                    screen.blit(icon_images[icon_index], 
                                (int(new_x) - NEW_CIRCLE_RADIUS, int(new_y) - NEW_CIRCLE_RADIUS))
                
                if new_circle_states[outer_index]["progress"] < 1:
                    new_circle_states[outer_index]["progress"] += step
    
    pygame.draw.circle(screen, CIRCLE_COLOR, CENTER, CENTER_RADIUS)
    pygame.draw.circle(screen, OUTLINE_COLOR, CENTER, CENTER_RADIUS, 2)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if math.sqrt((mouse_x - CENTER[0]) ** 2 + (mouse_y - CENTER[1]) ** 2) <= CENTER_RADIUS:
                expanded = not expanded
                animating = True
                active_index = None

            for i in range(len(labels)):
                angle = angles[i]
                circle_x = CENTER[0] + SURROUND_DISTANCE * math.cos(angle)
                circle_y = CENTER[1] + SURROUND_DISTANCE * math.sin(angle)
                
                if math.sqrt((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2) <= SURROUND_RADIUS:
                    active_index = i if active_index != i else None
                    break
            
            for i in range(8):
                for j in range(3):
                    outer_index = i * 3 + j  # Unique index for outer circles
                    angle = angles[i] + (j - 1) * (math.pi / 4)
                    circle_x = CENTER[0] + SURROUND_DISTANCE * math.cos(angles[i])
                    circle_y = CENTER[1] + SURROUND_DISTANCE * math.sin(angles[i])
                    outer_x = circle_x + NEW_CIRCLE_DISTANCE * math.cos(angle)
                    outer_y = circle_y + NEW_CIRCLE_DISTANCE * math.sin(angle)
                    
                    if math.sqrt((mouse_x - outer_x) ** 2 + (mouse_y - outer_y) ** 2) <= NEW_CIRCLE_RADIUS:
                        launch_app(outer_index)
                        break
    

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
