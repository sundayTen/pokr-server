import React from 'react';
import { StyleSheet } from 'react-native';
import WebView from 'react-native-webview';

import { View } from '../components/Themed';
import { RootTabScreenProps } from '../types';
import { HOST } from '../utils/webview';

export default function TabOneScreen({
	navigation,
}: RootTabScreenProps<'TabOne'>) {
	return (
		<View style={styles.container}>
			<WebView
				source={{
					uri: HOST,
				}}
			/>
		</View>
	);
}

const styles = StyleSheet.create({
	container: {
		flex: 1,
	},
});
