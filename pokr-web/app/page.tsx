'use client';
import globalStore from '../store/global';

export default function Home() {
	const { theme, changeTheme } = globalStore();

	const toggle = () => {
		if (theme === 'dark') {
			changeTheme('light');
			return;
		}
		changeTheme('dark');
	};
	return (
		<div>
			페이지
			<h1>{theme}</h1>
			<button onClick={toggle}>토글</button>
		</div>
	);
}
