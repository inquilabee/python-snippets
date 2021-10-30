from publishers import DataPublisher
from subscribers import DecimalViewer, HexViewer

if __name__ == '__main__':
    integer_publisher = DataPublisher("Integer Publisher")
    integer_observer = DecimalViewer()
    integer_publisher.subscribe(integer_observer)

    integer_publisher.data = 12
    integer_publisher.data = 10
    integer_publisher.data = 101
    integer_publisher.data = 21

    print("=" * 20)

    hex_observers = HexViewer()
    integer_publisher.subscribe(hex_observers)

    integer_publisher.data = 12
    integer_publisher.data = 10
    integer_publisher.data = 101
    integer_publisher.data = 21

    print("=" * 20)

    integer_publisher.unsubscribe(hex_observers)

    integer_publisher.data = 12
    integer_publisher.data = 10
    integer_publisher.data = 101
    integer_publisher.data = 21

    print("=" * 20)

    integer_publisher.unsubscribe(integer_observer)

    integer_publisher.data = 12
    integer_publisher.data = 10
    integer_publisher.data = 101
    integer_publisher.data = 21

    print("=" * 20)
