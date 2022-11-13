import './globals.css';

export default function RootLayout({
	children,
}: {
	children: React.ReactNode;
}) {
	return (
		<html lang="kn">
			{/* head 컴포넌트 아래에, 각 페이지별 head 컴포넌트에 적힌 내용은 이 컴포넌트의 내용을 상속함. */}
			<head>
				{/* 
        viewport 관련 기본 설정이 포함되어야 함
        링크 : https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag
      */}
				<meta name="viewport" content="width=device-width, initial-scale=1" />
			</head>
			<body>{children}</body>
		</html>
	);
}
