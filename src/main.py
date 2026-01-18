import pandas as pd
import numpy as np

class LearningAnalytics:
    def __init__(self):
        self.data = None
        self.predictions = None
    
    def load_data(self, filepath):
        """Загрузка данных студентов"""
        self.data = pd.read_csv(filepath)
        print(f"Загружено {len(self.data)} записей")
        return self.data
    
    def analyze_performance(self):
        """Анализ успеваемости"""
        if self.data is None:
            raise ValueError("Сначала загрузите данные!")
        
        analysis = {
            'average_grade': self.data['final_grade'].mean(),
            'min_grade': self.data['final_grade'].min(),
            'max_grade': self.data['final_grade'].max(),
            'at_risk_count': len(self.data[self.data['final_grade'] < 70])
        }
        return analysis
    
    def predict_grades(self):
        """Простое предсказание оценок (заглушка)"""
        if self.data is None:
            raise ValueError("Сначала загрузите данные!")
        
        # Простая логика предсказания
        self.predictions = self.data.copy()
        self.predictions['predicted_grade'] = (
            self.data['assignment_avg'] * 0.3 +
            self.data['quiz_avg'] * 0.2 +
            self.data['midterm_score'] * 0.5
        )
        return self.predictions

def main():
    """Основная функция"""
    print("=" * 50)
    print("Learning Analytics Dashboard")
    print("=" * 50)
    
    # Создаем экземпляр
    analyzer = LearningAnalytics()
    
    try:
        # Загружаем данные
        data = analyzer.load_data('data/sample_data.csv')
        print("\nПервые 5 записей:")
        print(data.head())
        
        # Анализируем
        stats = analyzer.analyze_performance()
        print("\nСтатистика успеваемости:")
        for key, value in stats.items():
            print(f"{key}: {value:.2f}")
        
        # Предсказываем
        predictions = analyzer.predict_grades()
        print("\nПредсказанные оценки (первые 5):")
        print(predictions[['student_id', 'final_grade', 'predicted_grade']].head())
        
        print("\n✅ Анализ завершен успешно!")
        
    except FileNotFoundError:
        print("❌ Файл данных не найден. Создайте data/sample_data.csv")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()
