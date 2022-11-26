'use client';
import globalStore from '../store/global';

const Home = () => {
  const { theme, changeTheme } = globalStore();

  const toggle = () => {
    if (theme === 'dark') {
      changeTheme('light');
      return;
    }
    changeTheme('dark');
  };

  return (
    <div>
      <h1>{theme}</h1>
      <button onClick={toggle}>토글</button>
    </div>
  );
};

export default Home;
