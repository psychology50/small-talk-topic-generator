import React from 'react';
import { ThemeProvider } from "./context/theme-provider";
import SmallTalkGenerator from './components/SmallTalkGenerator';

function App() {
  return (
    <ThemeProvider>
      <SmallTalkGenerator />
    </ThemeProvider>
  );
}

export default App;