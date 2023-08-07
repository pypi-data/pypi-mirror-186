try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets


class ProgressIndicator(QtWidgets.QWidget):
    m_angle = None
    m_timerId = None
    m_delay = None
    m_displayedWhenStopped = None
    m_color = None

    def __init__(self, parent):
        # Call parent class constructor first
        super().__init__(parent)

        # Initialize Qt Properties
        self.setProperties()

        # Intialize instance variables
        self.m_angle = 0
        self.m_timerId = -1
        self.m_delay = 40
        self.m_displayedWhenStopped = False
        self.m_color = QtCore.Qt.black

        # Set size and focus policy
        self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        # Show the widget
        self.show()

    def animationDelay(self):
        return self.delay

    def isAnimated(self):
        return (self.m_timerId != -1)

    def isDisplayedWhenStopped(self):
        return self.m_displayedWhenStopped

    def getColor(self):
        return self.color

    def sizeHint(self):
        return QtCore.QSize(20, 20)

    def startAnimation(self):
        self.m_angle = 0

        if self.m_timerId == -1:
            self.m_timerId = self.startTimer(self.m_delay)

    def stopAnimation(self):
        if self.m_timerId != -1:
            self.killTimer(self.m_timerId)

        self.m_timerId = -1
        self.update()

    def setAnimationDelay(self, delay):
        if self.m_timerId != -1:
            self.killTimer(self.m_timerId)

        self.m_delay = delay

        if self.m_timerId != -1:
            self.m_timerId = self.startTimer(self.m_delay)

    def setDisplayedWhenStopped(self, state):
        self.m_displayedWhenStopped = state
        self.update()

    def setColor(self, color):
        self.m_color = color
        self.update()

    def timerEvent(self, event):
        self.m_angle = (self.m_angle + 30) % 360
        self.update()

    def paintEvent(self, event):
        if (not self.m_displayedWhenStopped) and (not self.isAnimated()):
            return

        width = min(self.width(), self.height())

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        outerRadius = (width - 1) * 0.5
        innerRadius = (width - 1) * 0.5 * 0.38

        capsuleHeight = outerRadius - innerRadius
        capsuleWidth = capsuleHeight * .23 if (width > 32) else capsuleHeight * .35
        capsuleRadius = capsuleWidth / 2

        color = QtGui.QColor(self.m_color)
        for i in range(0, 12):
            if self.isAnimated():
                color.setAlphaF(1.0 - (i / 12.0))
            else:
                color.setAlphaF(0.2)

            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(color)
            painter.save()
            painter.translate(self.rect().center())
            painter.rotate(self.m_angle - (i * 30.0))
            painter.drawRoundedRect(capsuleWidth * -0.5, (innerRadius + capsuleHeight) * -1, capsuleWidth,
                                    capsuleHeight, capsuleRadius, capsuleRadius)
            painter.restore()

    def setProperties(self):
        self.delay = QtCore.Property(int, self.animationDelay, self.setAnimationDelay)
        self.displayedWhenStopped = QtCore.Property(bool, self.isDisplayedWhenStopped, self.setDisplayedWhenStopped)
        self.color = QtCore.Property(QtGui.QColor, self.getColor, self.setColor)
