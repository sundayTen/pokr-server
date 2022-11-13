import Head from 'next/head';
import React from 'react';

interface SeoProps {
	title: string;
}

const Seo = (props: SeoProps) => {
	return (
		<Head>
			<title>{`${props.title} | PKR`}</title>
			<meta name="pkr" content="Personal OKR" />
			<link rel="icon" href="/favicon.ico" />
		</Head>
	);
};

export default Seo;
