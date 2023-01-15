import { useState, useEffect } from 'react';
import { useMediaQuery } from 'react-responsive';

/**
 * 반응형 pc, mobile 체크
 * @param isRN
 */
const useIsMobile = (isRN?: any) => {
  const [isMobile, setIsMobile] = useState<boolean>(false);
  const isTabletOrMobile = useMediaQuery({ query: '(max-width: 1224px)' });

  // isRN 처리

  useEffect(() => {
    setIsMobile(isTabletOrMobile);
  }, [isTabletOrMobile]);

  return isMobile;
};

export default useIsMobile;
