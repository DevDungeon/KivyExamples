from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class PongPaddle(Widget):
    pass


class PongBallWidget(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGameWidget(Widget):

    def on_touch_down(self, touch):
        pass
        if touch.x < self.width / 2:
            self.player1.center_y = touch.y
        if touch.x > self.width / 2:
            self.player2.center_y = touch.y

    def kickoff(self):
        self.ball.velocity_x = 4
        self.ball.velocity_y = 4

    def update(self, delta_time):
        self.ball.move()
        if self.ball.collide_widget(self.player1) or self.ball.collide_widget(self.player2):
            self.ball.velocity_x *= -1

        # Bounce it off the walls
        if (self.ball.top > self.height) or (self.ball.y < 0):
            self.ball.velocity_y *= -1
        if (self.ball.right > self.width) or (self.ball.x < 0):
            self.ball.velocity_x *= -1


class PongApp(App):
    def build(self):
        game = PongGameWidget()
        Clock.schedule_interval(game.update, 1.0/60.0)
        game.kickoff()
        return game


if __name__ == '__main__':
    pong = PongApp()
    pong.run()
