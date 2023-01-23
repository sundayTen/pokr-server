'use client';
import './globals.scss';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Header from '@components/common/header/Header';
import Aside from '@components/common/aside';
import useIsMobile from 'hooks/useIsMobile';
import MobileHeader from '@components/common/header/MobileHeader';

const queryClient = new QueryClient();

interface GlobalLayout {
  children: React.ReactNode;
}

const Layout = ({ children }: GlobalLayout) => {
  const { isMobile } = useIsMobile();

  return (
    <html lang="kn">
      {/* head 컴포넌트 아래에, 각 페이지별 head 컴포넌트에 적힌 내용은 이 컴포넌트의 내용을 상속함. */}
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body>
        <QueryClientProvider client={queryClient}>
          {/* The rest of your application */}
          <ReactQueryDevtools initialIsOpen={false} />
          {isMobile ? <MobileHeader /> : <Header />}
          <div id="container">
            {!isMobile && <Aside />}
            {children}
          </div>
        </QueryClientProvider>
      </body>
    </html>
  );
};

export default Layout;
