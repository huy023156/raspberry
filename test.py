import RPi.GPIO as GPIO
import pygame
import sys
import time

# Thiết lập GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Đặt chân GPIO kết nối với bóng đèn LED (giả sử dùng GPIO17)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ mô phỏng
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mô phỏng Bóng đèn LED')

# Màu sắc
black = (0, 0, 0)
yellow = (255, 255, 0)

# Trạng thái bóng đèn
led_on = False

# Hàm bật đèn LED
def turn_on_led():
    GPIO.output(led_pin, GPIO.HIGH)

# Hàm tắt đèn LED
def turn_off_led():
    GPIO.output(led_pin, GPIO.LOW)

# Vòng lặp chính
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                GPIO.cleanup()
                sys.exit()

            # Nhấn phím SPACE để bật/tắt bóng đèn
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    led_on = not led_on
                    if led_on:
                        turn_on_led()
                    else:
                        turn_off_led()

        # Làm sạch màn hình
        screen.fill(black)

        # Vẽ bóng đèn mô phỏng
        if led_on:
            pygame.draw.circle(screen, yellow, (screen_width // 2, screen_height // 2), 50)
        else:
            pygame.draw.circle(screen, black, (screen_width // 2, screen_height // 2), 50)

        # Cập nhật màn hình
        pygame.display.flip()
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    # Dọn dẹp GPIO khi thoát chương trình
    GPIO.cleanup()
    pygame.quit()
    sys.exit()
