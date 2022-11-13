/**
 * 전역객체가 존재하는지 확인하여 Client Side인지 확인합니다.
 */
const isClientSide = () => {
	return typeof window === 'undefined';
};

const isSSR = () =>
	isClientSide() ||
	!window.navigator ||
	/ServerSideRendering|^Deno\//.test(window.navigator.userAgent);

/**
 * Android인지 확인합니다.
 */
const isAndroid = (userAgent: string) => {};

/**
 * Ios인지 확인합니다.
 */
const isIos = (userAgent: string) => {};

export { isClientSide, isSSR, isAndroid, isIos };
