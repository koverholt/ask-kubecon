/** @type {import('tailwindcss').Config}*/
const config = {
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		'./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}',
		'./node_modules/flowbite-svelte-blocks/**/*.{html,js,svelte,ts}'
	],
	plugins: [require('flowbite/plugin'), require('flowbite-typography')],
	darkMode: 'class',
	theme: {
		extend: {
			colors: {
				primary: {
					50: '#f4f5f9',
					100: '#ebedf4',
					200: '#daddeb',
					300: '#c3c7de',
					400: '#a9add0',
					500: '#9394c1',
					600: '#7f7caf',
					700: '#a9add0',
					800: '#59577c',
					900: '#4b4a65',
					950: '#2c2b3b'
				}
			}
		}
	}
};

module.exports = config;
