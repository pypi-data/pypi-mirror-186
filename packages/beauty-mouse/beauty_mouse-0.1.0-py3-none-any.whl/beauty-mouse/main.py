from enum import Enum, auto
from time import sleep
from pynput.mouse import Button, Controller
from secrets import randbelow
import HIServices

if not HIServices.AXIsProcessTrusted():
    print(
        "This process is NOT a trusted accessibility client, so pynput will not "
        "function properly. Please grant accessibility access for this app in "
        "System Preferences."
    )


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class JiggleClicker:
    def __init__(
        self,
        mouse: Controller,
        min_duration=1,
        max_duration=10,
        speed=5,
        smoothing=0.05,
        debounce=20,
    ) -> None:
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.speed = speed
        self.smoothing = smoothing
        self.mouse = mouse
        self.debounce = debounce

    def _dirToOffset(self, d: Direction) -> list[int]:
        match d:
            case Direction.UP:
                return [0, 1 * self.speed]
            case Direction.DOWN:
                return [0, -1 * self.speed]
            case Direction.LEFT:
                return [1 * self.speed, 0]
            case Direction.RIGHT:
                return [-1 * self.speed, 0]

    def smoothMoveTo(self, x, y):
        cpos = self.mouse.position
        cx = int(cpos[0])
        cy = int(cpos[1])
        while (
            cx < x - self.debounce
            or cx > x + self.debounce
            or cy < y - self.debounce
            or cy > y + self.debounce
        ):
            if cx < x - self.debounce:
                self.mouse.move(*self._dirToOffset(Direction.LEFT))
                sleep(self.smoothing)
            elif cx > x + self.debounce:
                self.mouse.move(*self._dirToOffset(Direction.RIGHT))
                sleep(self.smoothing)
            if cy < y - self.debounce:
                self.mouse.move(*self._dirToOffset(Direction.UP))
                sleep(self.smoothing)
            elif cy > y + self.debounce:
                self.mouse.move(*self._dirToOffset(Direction.DOWN))
                sleep(self.smoothing)
            cpos = self.mouse.position
            cx = int(cpos[0])
            cy = int(cpos[1])
            print(x, "|", cx, "-", y, "|", cy)

    def changeChapter(
        self,
    ):
        pass

    def clickVideo(
        self,
    ):
        pass

    def clickNop(
        self,
    ):
        pass


def main():
    mouse = Controller()
    jiggler = JiggleClicker(mouse, speed=0.35, smoothing=0.0001)
    for _ in range(0, 20):
        mouse.press(Button.left)
        rx = 100 + randbelow(1000)
        ry = 100 + randbelow(1000)
        jiggler.smoothMoveTo(rx, ry)
        mouse.release(Button.left)
        sleep(1)


if __name__ == "__main__":
    main()
