#include <SFML/Graphics.hpp>
#include <complex>

int mandelbrot() {
	const int width = 800, height = 600;
	sf::RenderWindow window (sf::VideoMode(width,height), "Mandelbrot Fractal");
	
	sf::Image image;
	image.create(width, height);

	for (int y = 0; y < height; ++y) {
		for (int x = 0; x < width; ++x) {
			std::complex<double> c (
				(x - width/2.0) * 4.0/width,
				(y - height/2.0) * 4.0/width
			);
			std::complex<double> z = 0;

			int iterations = 0;
			while(abs(z) < 2.0 && iterations < 255) {
				z = z * z + c;
				++iterations;
			}

			sf::Color color(iterations, iterations, iterations);
			image.setPixel(x, y, color);
		}
	}

	sf::Texture texture;
	texture.loadFromImage(image);
	sf::Sprite sprite(texture);

	while (window.isOpen()) {
		sf::Event event;
		while (window.pollEvent(event))
			if (event.type == sf::Event::Closed)
				window.close();

		window.clear();
		window.draw(sprite);
		window.display();
	}
	
	return 0;
}

int main() {
	return mandelbrot();
}