'use client';

import React from 'react';
import DashBoardHeader from './header';
import DashBoardPeriod from './period';
import styles from '@components/dashboard/header/DashBoardHeader.module.scss';
import DashBoardGraph from './graph';

const DashBoard = () => {
  return (
    <div className={styles.dashBoard}>
      <DashBoardHeader />
      <DashBoardPeriod />
      <DashBoardGraph />
    </div>
  );
};

export default DashBoard;
