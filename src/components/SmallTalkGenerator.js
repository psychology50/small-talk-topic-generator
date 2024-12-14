import React, { useState, useEffect } from 'react';
import { Card, CardContent } from './ui/card';
import { Button } from './ui/button';
import { ThemeToggle } from './theme-toggle';
import { Shuffle, Menu, Gauge } from 'lucide-react';
import { CATEGORIES, DIFFICULTIES, getTopicsByDifficulty } from '../constants/topics';

const SmallTalkGenerator = () => {
    const [selectedCategories, setSelectedCategories] = useState([CATEGORIES.ALL]);
    const [selectedDifficulties, setSelectedDifficulties] = useState(['all']);
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
        let availableTopics = [];
        
        // 선택된 카테고리들에서 토픽 수집
        if (selectedCategories.includes(CATEGORIES.ALL)) {
          // All Topics이 선택된 경우
          Object.values(CATEGORIES)
            .filter(cat => cat !== CATEGORIES.ALL)
            .forEach(category => {
              if (selectedDifficulties.includes('all')) {
                // 모든 난이도의 토픽 추가
                DIFFICULTIES.forEach(diff => {
                  const topics = getTopicsByDifficulty(diff)[category] || [];
                  availableTopics = [...availableTopics, ...topics];
                });
              } else {
                // 선택된 난이도의 토픽만 추가
                selectedDifficulties.forEach(diff => {
                  const topics = getTopicsByDifficulty(diff)[category] || [];
                  availableTopics = [...availableTopics, ...topics];
                });
              }
            });
        } else {
          // 특정 카테고리들이 선택된 경우
          selectedCategories.forEach(category => {
            if (selectedDifficulties.includes('all')) {
              // 모든 난이도의 토픽 추가
              DIFFICULTIES.forEach(diff => {
                const topics = getTopicsByDifficulty(diff)[category] || [];
                availableTopics = [...availableTopics, ...topics];
              });
            } else {
              // 선택된 난이도의 토픽만 추가
              selectedDifficulties.forEach(diff => {
                const topics = getTopicsByDifficulty(diff)[category] || [];
                availableTopics = [...availableTopics, ...topics];
              });
            }
          });
        }
  
        // 랜덤하게 토픽 선택
        if (availableTopics.length > 0) {
          const randomTopic = availableTopics[Math.floor(Math.random() * availableTopics.length)];
          setCurrentTopic(randomTopic.question);
        } else {
          setCurrentTopic("No topics found for selected criteria. Try different options!");
        }
      } catch (error) {
        console.error('Error generating topic:', error);
        setCurrentTopic("Error generating topic. Please try again!");
      }
    };

      const handleCategoryClick = (category) => {
        if (category === CATEGORIES.ALL) {
          // All Topics 선택 시 다른 모든 선택 해제
          setSelectedCategories([CATEGORIES.ALL]);
        } else {
          let newCategories = [...selectedCategories];
          
          if (selectedCategories.includes(CATEGORIES.ALL)) {
            // All Topics이 선택된 상태에서 다른 카테고리 선택 시
            newCategories = [category];
          } else if (selectedCategories.includes(category)) {
            // 이미 선택된 카테고리 클릭 시 제거
            // 단, 마지막 하나 남은 카테고리는 제거 불가
            if (selectedCategories.length > 1) {
              newCategories = selectedCategories.filter(c => c !== category);
            }
          } else {
            // 새로운 카테고리 추가
            newCategories = [...selectedCategories, category];
          }
          
          setSelectedCategories(newCategories);
        }
      };

      const handleDifficultyClick = (difficulty) => {
        if (difficulty === 'all') {
          // All Levels 선택 시 다른 모든 선택 해제
          setSelectedDifficulties(['all']);
        } else {
          let newDifficulties = [...selectedDifficulties];
          
          if (selectedDifficulties.includes('all')) {
            // All Levels가 선택된 상태에서 다른 난이도 선택 시
            newDifficulties = [difficulty];
          } else if (selectedDifficulties.includes(difficulty)) {
            // 이미 선택된 난이도 클릭 시 제거
            // 단, 마지막 하나 남은 난이도는 제거 불가
            if (selectedDifficulties.length > 1) {
              newDifficulties = selectedDifficulties.filter(d => d !== difficulty);
            }
          } else {
            // 새로운 난이도 추가
            newDifficulties = [...selectedDifficulties, difficulty];
          }
          
          setSelectedDifficulties(newDifficulties);
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
              variant={selectedCategories.includes(CATEGORIES.ALL) ? 'default' : 'outline'}
              onClick={() => handleCategoryClick(CATEGORIES.ALL)}
              className="capitalize w-full md:w-auto"
            >
              All Topics
            </Button>
            {Object.values(CATEGORIES).filter(cat => cat !== CATEGORIES.ALL).map((category) => (
              <Button
                key={category}
                variant={selectedCategories.includes(category) ? 'default' : 'outline'}
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
                variant={selectedDifficulties.includes('all') ? 'default' : 'outline'}
                onClick={() => handleDifficultyClick('all')}
                className="capitalize w-full md:w-auto"
              >
                All Levels
              </Button>
              {DIFFICULTIES.map((difficulty) => (
                <Button
                  key={difficulty}
                  variant={selectedDifficulties.includes(difficulty) ? 'default' : 'outline'}
                  onClick={() => handleDifficultyClick(difficulty)}
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