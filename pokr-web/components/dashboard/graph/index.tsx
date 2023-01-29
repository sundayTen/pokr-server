import React from 'react';
import styles from '@components/dashboard/graph/DashBoardGraph.module.scss';
import {
  ResponsiveContainer,
  AreaChart,
  Tooltip,
  Area,
  CartesianGrid,
  XAxis,
  YAxis,
} from 'recharts';
const data = [
  { name: '1월', '사용자 평균': 10, '이용자 평균 달성도': 53 },
  { name: '2월', '사용자 평균': 14, '이용자 평균 달성도': 40 },
  { name: '3월', '사용자 평균': 30, '이용자 평균 달성도': 42 },
  { name: '4월', '사용자 평균': 30, '이용자 평균 달성도': 29 },
  { name: '5월', '사용자 평균': 50, '이용자 평균 달성도': 21 },
  { name: '6월', '사용자 평균': 0, '이용자 평균 달성도': 0 },
];

const Graph = () => {
  return (
    <section className={styles.root}>
      <div className={styles.container}>
        <h1>반기 달성 지표</h1>
        <p>이번 달은 전체 사용자의 평균 보다 15% 높게 달성했어요!</p>
      </div>

      <div className={styles.timer}>2023년 상반기 62일 남음</div>
      <ResponsiveContainer width={'100%'} aspect={4}>
        <AreaChart data={data} margin={{ top: 20, bottom: 0 }}>
          <defs>
            <linearGradient id="color-my'" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#9be8cd" stopOpacity={0.5} />
              <stop offset="100%" stopColor="#9be8cd" stopOpacity={0} />
            </linearGradient>
            <linearGradient id="color-user-average" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#18cb8c" stopOpacity={0.5} />
              <stop offset="100%" stopColor="#18cb8c" stopOpacity={0} />
            </linearGradient>
          </defs>
          <XAxis dataKey="name" />
          <YAxis tickCount={6} />
          <CartesianGrid strokeDasharray="3 3" vertical={false} />
          <Tooltip content={CustomTooltip} />
          <Area
            type="monotone"
            dataKey="사용자 평균"
            stroke="#9be8cd"
            strokeWidth={3}
            fillOpacity={1}
            fill="url(#color-my)"
          />
          <Area
            type="monotone"
            dataKey="이용자 평균 달성도"
            stroke="#82ca9d"
            strokeWidth={3}
            fillOpacity={1}
            fill="url(#color-user-average)"
          />
        </AreaChart>
      </ResponsiveContainer>
    </section>
  );
};

export default Graph;

const CustomTooltip = (props) => {
  const { active, payload, label } = props;
  if (active && payload && payload.length >= 2) {
    return (
      <div className={styles.tooltip}>
        <p className={styles.label}>{`${label} 1일 ~ ${label} 30일`}</p>
        <div className={styles['chip-container']}>
          <div className={styles['chip-me']} />
          <span
            className={styles.desc}
          >{`나의 평균 : ${payload[0].value}`}</span>
        </div>
        <div className={styles['chip-container']}>
          <div className={styles['chip-avg']} />
          <span
            className={styles.desc}
          >{`사용자 평균 : ${payload[1].value}`}</span>
        </div>
      </div>
    );
  }

  return <></>;
};
