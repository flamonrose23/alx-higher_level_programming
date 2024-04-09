#!/usr/bin/node
module.exports = class Rectangle {
	constructor (h, w) {
		if (h > 0 && w > 0) { [this.height, this.width] = [h, w]; }
	}

	print () {
		for (let a = 0; a < this.width; a++) console.log('X'.repeat(this.height));
	}
};
