export const isRealString = (string: string | number) => {
	if (typeof string === 'string') {
		return true;
	}

	return false;
};
