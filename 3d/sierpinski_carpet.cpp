#include <SFML/Graphics.hpp>
#include <complex>
#include <iostream>
#include <cmath>

const int CUBE_1 = 3;
const int CUBE_2 = 3*3;
const float CUBE_N1 = pow(3,-1);

struct Point {
	float x, y;
};

struct Triangle {
	Point a, b, c;
};

struct Square {
	Triangle a, b;
};

Triangle getUnitTriangle() {
	Triangle t;

	t.a = {0.0f, 0.0f};
	t.b = {1.0f, 0.0f};
	t.c = {0.0f, 1.0f};

	return t;
}

Square getUnitSquare() {
	Triangle tri1 = getUnitTriangle();
	Triangle tri2 = getUnitTriangle();

	// std::cout << tri1.a.x << ", " << tri1.a.y << std::endl;
	// std::cout << tri1.b.x << ", " << tri1.b.y << std::endl;
	// std::cout << tri1.c.x << ", " << tri1.c.y << std::endl;

	Square square;
	square.a = tri1;
	square.b = tri2;

	return square;
}


int sierpinski_carpet() {
	const int width = 800, height = 600;
	sf::RenderWindow window (sf::VideoMode(width,height), "Sierpinski Carpet");
	
	sf::Image image;
	image.create(width, height);
	
	Square unit_square = getUnitSquare();
	
	std::cout << CUBE_N1 << std::endl;

	sf::Color color(0,255,0);
	int scale = 100;
	int transform = 300;
	image.setPixel(unit_square.a.a.x * scale + transform, unit_square.a.a.y * scale + transform, color);
	image.setPixel(unit_square.a.b.x * scale + transform, unit_square.a.b.y * scale + transform, color);
	image.setPixel(unit_square.a.c.x * scale + transform, unit_square.a.c.y * scale + transform, color);

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

	// std::cout << CUBE_N1 << std::endl;
	
	// need to redo unit square
	//
	
	return 0;
}

int main() {
	return sierpinski_carpet();
}
