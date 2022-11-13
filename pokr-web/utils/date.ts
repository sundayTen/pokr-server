import dayjs from 'dayjs';

export const SECOND_TO_MS = 1000;
export const MINUTE_UNIT = 60;
export const HOUR_UNIT = 60;

export const YYYYMMDD = (date: string) => dayjs(date).format('YYYY.MM.DD');
