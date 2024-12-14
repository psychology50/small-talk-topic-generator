import React, { useState, useEffect } from 'react';
import { Card, CardContent } from './ui/card';
import { Button } from './ui/button';
import { ThemeToggle } from './theme-toggle';
import { Shuffle, Menu, Gauge } from 'lucide-react';
import { CATEGORIES, DIFFICULTIES, getRandomTopic, getTopicsByDifficulty } from '../constants/topics';

const SmallTalkGenerator = () => {
    const [selectedCategory, setSelectedCategory] = useState(CATEGORIES.ALL);
    const [selectedDifficulty, setSelectedDifficulty] = useState('all');
    const [currentTopic, setCurrentTopic] = useState('Click the button to get a conversation starter!');
    const [isMobile, setIsMobile] = useState(false);
    const [showCategories, setShowCategories] = useState(true);
    const [showDifficulty, setShowDifficulty] = useState(true);  // 추가
  
    useEffect(() => {
      const checkMobile = () => {
        const isMobileView = window.innerWidth < 768;
        setIsMobile(isMobileView);
        if (!isMobileView) {
          setShowCategories(true);
          setShowDifficulty(true);
        }
      };
  
      checkMobile();
      window.addEventListener('resize', checkMobile);
      return () => window.removeEventListener('resize', checkMobile);
    }, []);
  
    const generateNewTopic = () => {
        try {
          let topic;
          if (selectedDifficulty === 'all') {
            topic = getRandomTopic(selectedCategory);
          } else {
            const difficultyTopics = getTopicsByDifficulty(selectedDifficulty);
            if (selectedCategory === CATEGORIES.ALL) {
              const allTopics = Object.values(difficultyTopics).flat();
              topic = allTopics[Math.floor(Math.random() * allTopics.length)];
            } else {
              const categoryTopics = difficultyTopics[selectedCategory] || [];
              topic = categoryTopics[Math.floor(Math.random() * categoryTopics.length)];
            }
          }
          
          if (topic) {
            setCurrentTopic(topic.question);
          } else {
            setCurrentTopic("No topic found for selected category and difficulty. Try different options!");
          }
        } catch (error) {
          console.error('Error generating topic:', error);
          setCurrentTopic("Error generating topic. Please try again!");
        }
      };

  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
    if (isMobile) {
      setShowCategories(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900 p-4 md:p-8">
      <ThemeToggle />
      <div className="max-w-2xl mx-auto space-y-4 md:space-y-6">
        <h1 className="text-2xl md:text-3xl font-bold text-center text-gray-800 dark:text-gray-100">
          Small Talk Topic Generator
        </h1>
        
        {/* Categories Toggle Button */}
        {isMobile && (
          <div className="flex justify-center">
            <Button
              variant="outline"
              onClick={() => setShowCategories(!showCategories)}
              className="w-full md:w-auto"
            >
              <Menu className="w-4 h-4 mr-2" />
              {showCategories ? 'Hide Categories' : 'Show Categories'}
            </Button>
          </div>
        )}

        {/* Categories Section */}
        {showCategories && (
        <div className="p-4 bg-white dark:bg-gray-800 rounded-lg shadow-sm">
        <h2 className="text-lg font-semibold mb-4 text-gray-800 dark:text-gray-100 flex items-center justify-center gap-2">
          <Menu className="w-5 h-5" />
            Categories
            </h2>
            <div className="flex flex-col md:flex-row flex-wrap justify-center gap-2">
            <Button
                variant={selectedCategory === CATEGORIES.ALL ? 'default' : 'outline'}
                onClick={() => handleCategoryClick(CATEGORIES.ALL)}
                className="w-full md:w-auto"
            >
                All Topics
            </Button>
            {Object.values(CATEGORIES).filter(cat => cat !== CATEGORIES.ALL).map((category) => (
                <Button
                key={category}
                variant={selectedCategory === category ? 'default' : 'outline'}
                onClick={() => handleCategoryClick(category)}
                className="capitalize w-full md:w-auto"
                >
                {category}
                </Button>
            ))}
            </div>
        </div>
        )}

        {/* Difficulty Section */}
        {showDifficulty && (
        <div className="p-4 bg-white dark:bg-gray-800 rounded-lg shadow-sm">
        <h2 className="text-lg font-semibold mb-4 text-gray-800 dark:text-gray-100 flex items-center justify-center gap-2">
          <Gauge className="w-5 h-5" />
            Difficulty Level
            </h2>
            <div className="flex flex-col md:flex-row flex-wrap justify-center gap-2">
            <Button
                variant={selectedDifficulty === 'all' ? 'default' : 'outline'}
                onClick={() => setSelectedDifficulty('all')}
                className="w-full md:w-auto"
            >
                All Levels
            </Button>
            {DIFFICULTIES.map((difficulty) => (
                <Button
                key={difficulty}
                variant={selectedDifficulty === difficulty ? 'default' : 'outline'}
                onClick={() => setSelectedDifficulty(difficulty)}
                className="capitalize w-full md:w-auto"
                >
                {difficulty}
                </Button>
            ))}
            </div>
        </div>
        )}

        <Card className="shadow-lg dark:bg-gray-800">
        <CardContent className="p-4 md:p-6">
            <p className="text-lg md:text-xl font-medium text-center text-gray-800 dark:text-gray-100 min-h-[3rem] leading-relaxed">
            {currentTopic}
            </p>
        </CardContent>
        </Card>

        <div className="flex justify-center">
          <Button
            size="lg"
            onClick={generateNewTopic}
            className="gap-2 w-full md:w-auto"
          >
            <Shuffle className="w-4 h-4" />
            Get New Topic
          </Button>
        </div>
      </div>
    </div>
  );
};

export default SmallTalkGenerator;