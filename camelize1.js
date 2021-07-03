const dashy = 'dem-tings-dem'

const camelize = (str) => {
	return str
		.split('-') // splits 'this-that-this' str into arr 
			//	['this', 'that', 'word']
		.map((word, index) => index == 0 ? word : word[0].toUpperCase()
		+ word.slice(1)
		)	 // capitlize first letters of all arr items except first
			// converts ['this', 'that', 'word'] into ['this', 'Long', 'Word'			
		.join(''); // joins ['this', 'That', 'Word'] into 'thisThatWord'
		}

console.log(camelize(dashy))	
