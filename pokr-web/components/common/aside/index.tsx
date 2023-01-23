import React from 'react';
import styles from '@components/common/aside/Aside.module.scss';
import AutoHeightImage from '@components/common/image';
import Link from 'next/link';

const Aside = () => {
  return (
    <div className={styles.root}>
      <Link href="/" className={styles.selected}>
        <AutoHeightImage
          src="/images/dash-board.png"
          alt="대시보드"
          width={24}
          height={24}
        />
        대시보드
      </Link>
      <Link href="/">
        <AutoHeightImage
          src="/images/goal-management.png"
          alt="목표관리"
          width={24}
          height={24}
        />
        목표관리
      </Link>
      <Link href="/">
        <AutoHeightImage
          src="/images/memoir.png"
          alt="회고록"
          width={24}
          height={24}
        />
        회고록
      </Link>
    </div>
  );
};

export default Aside;
