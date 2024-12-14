import React, { useState, useEffect } from 'react';
import { Card, CardContent } from './ui/card';
import { Button } from './ui/button';
import { Shuffle, Menu } from 'lucide-react';
import { CATEGORIES, getRandomTopic } from '../constants/topics';

const SmallTalkGenerator = () => {
  const [selectedCategory, setSelectedCategory] = useState(CATEGORIES.ALL);
  const [currentTopic, setCurrentTopic] = useState('Click the button to get a conversation starter!');
  const [isMobile, setIsMobile] = useState(false);
  const [showCategories, setShowCategories] = useState(true);

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768);
      setShowCategories(window.innerWidth >= 768);
    };

    checkMobile();
    window.addEventListener('resize', checkMobile);
    return () => window.removeEventListener('resize', checkMobile);
  }, []);
  
  const generateNewTopic = () => {
    const topic = getRandomTopic(selectedCategory);
    setCurrentTopic(topic.question);
  };

  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
    if (isMobile) {
      setShowCategories(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4 md:p-8">
      <div className="max-w-2xl mx-auto space-y-4 md:space-y-6">
        <h1 className="text-2xl md:text-3xl font-bold text-center text-gray-800">
          Small Talk Topic Generator
        </h1>
        
        {isMobile && (
          <div className="flex justify-center">
            <Button
              variant="outline"
              onClick={() => setShowCategories(!showCategories)}
              className="w-full md:w-auto mb-2"
            >
              <Menu className="w-4 h-4 mr-2" />
              {showCategories ? 'Hide Categories' : 'Show Categories'}
            </Button>
          </div>
        )}

        {showCategories && (
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
        )}

        <Card className="shadow-lg">
          <CardContent className="p-4 md:p-6">
            <p className="text-base md:text-lg text-center text-gray-700 min-h-[3rem]">
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