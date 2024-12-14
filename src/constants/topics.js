import workTopics from '../data/topics/work.json';
import hobbiesTopics from '../data/topics/hobbies.json';
import travelTopics from '../data/topics/travel.json';
import entertainmentTopics from '../data/topics/entertainment.json';
import foodTopics from '../data/topics/food.json';
import techTopics from '../data/topics/tech.json';
import lifestyleTopics from '../data/topics/lifestyle.json';

export const CATEGORIES = {
  ALL: 'all',
  WORK: 'work',
  HOBBIES: 'hobbies',
  TRAVEL: 'travel',
  ENTERTAINMENT: 'entertainment',
  FOOD: 'food',
  TECH: 'tech',
  LIFESTYLE: 'lifestyle'
};

export const getAllTopics = () => {
    const allTopics = {
      [CATEGORIES.WORK]: workTopics.topics,
      [CATEGORIES.HOBBIES]: hobbiesTopics.topics,
      [CATEGORIES.TRAVEL]: travelTopics.topics,
      [CATEGORIES.ENTERTAINMENT]: entertainmentTopics.topics,
      [CATEGORIES.FOOD]: foodTopics.topics,
      [CATEGORIES.TECH]: techTopics.topics,
      [CATEGORIES.LIFESTYLE]: lifestyleTopics.topics,
    };
    return allTopics;
  };

  export const getRandomTopic = (category) => {
    const allTopics = getAllTopics();
    
    if (category === CATEGORIES.ALL) {
      const allQuestions = Object.values(allTopics).flat();
      return allQuestions[Math.floor(Math.random() * allQuestions.length)];
    }
    
    const categoryTopics = allTopics[category];
    return categoryTopics[Math.floor(Math.random() * categoryTopics.length)];
  };
  
  // 추가 유틸리티 함수들
  export const getTopicsByDifficulty = (difficulty) => {
    const allTopics = getAllTopics();
    return Object.values(allTopics)
      .flat()
      .filter(topic => topic.difficulty === difficulty);
  };
  
  export const getTopicsByTags = (tags) => {
    const allTopics = getAllTopics();
    return Object.values(allTopics)
      .flat()
      .filter(topic => topic.tags.some(tag => tags.includes(tag)));
  };