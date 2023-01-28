import React from 'react';
import Navbar from './navbar';
import { Header, MobileHeader } from '@components/common/GlobalLayout/header';
import useIsMobile from '@hooks/useIsMobile';

interface GlobalLayoutProps {
  children: React.ReactNode;
}

const GlobalLayout = ({ children }: GlobalLayoutProps) => {
  const { isMobile, isApp } = useIsMobile();
  return (
    <main>
      {isMobile ? isApp ? <></> : <MobileHeader /> : <Header />}
      {!isMobile && <Navbar />}
      {children}
    </main>
  );
};

export default GlobalLayout;
