import React from 'react';
import Navbar from './navbar';
import { Header, MobileHeader } from '@components/common/GlobalLayout/header';
import useIsMobile from '@hooks/useIsMobile';
import styles from '@components/common/GlobalLayout/GlobalLayout.module.scss';

interface GlobalLayoutProps {
  children: React.ReactNode;
}

const GlobalLayout = ({ children }: GlobalLayoutProps) => {
  const { isMobile, isApp } = useIsMobile();
  return (
    <main className={styles.root}>
      {isMobile ? isApp ? <></> : <MobileHeader /> : <Header />}
      {!isMobile && <Navbar />}
      {children}
    </main>
  );
};

export default GlobalLayout;
