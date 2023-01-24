import { useNavigation } from '@react-navigation/native';
import WebView, { WebViewMessageEvent } from 'react-native-webview';

export const HOST = 'http://localhost:3000'; // 추후 환경별로 호스트를 변경해주면 됨

/**
 * Web에서 RN으로 메시지를 보낼 수 있도록 메소드를 심는 자바스크립트 코드입니다.
 * Web을 호출하는 시점에 주입하여 Web에서 글로벌 객체의 메소드처럼 사용합니다.
 */
export const injectedJsForPostMessage = `
	(function() {
    window.ReactNativeWebView.postMessage(JSON.stringify(window.location));
	})();
	true;
`;

/**
 * Web으로부터 전달받은 메시지를 핸들링합니다.
 */
export const onMessage = (event: WebViewMessageEvent) => {
	const navigation = useNavigation();
	const { navigate, replace, canGoBack, goBack } = navigation;

	const { target, navigationData } = JSON.parse(
		event.nativeEvent.data,
	) as COMMON_ONMESSAGE_DATA;

	switch (target) {
		case 'navigate':
			navigate(navigationData.stack, navigationData.params);
			break;
		case 'replace':
			replace(navigationData.stack, navigationData.params);
			break;
		case 'goBack':
			if (canGoBack()) {
				goBack();
				return;
			}
			break;
		default:
			break;
	}
};

/**
 * 데이터를 웹뷰에 전달합니다.
 * Web에서는 이벤트 리스너에서 처리합니다.
 */
export const sendDataToWebview = (
	webviewRef: React.RefObject<WebView>,
	dataToSend: any,
) => {
	webviewRef.current?.postMessage(
		JSON.stringify({
			...dataToSend,
		}),
	);
};

interface COMMON_ONMESSAGE_DATA {
	target: 'navigate' | 'replace' | 'goBack' | 'onLoad';
	navigationData: {
		stack: string;
		params: any;
	};
}
