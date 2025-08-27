from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re
import json
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import tempfile
import os


class AIModel:
    def __init__(self):
        self.model = None
        self.text_vectorizer = None
        self.capabilities = {
            'image_generation': True,
            'pdf_creation': True,
            'text_analysis': True,
            'content_creation': True
        }

    def train_model(self, X, y):
        """Train a sophisticated AI model with multiple capabilities."""
        # Main classification pipeline
        pipeline = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200))
        pipeline.fit(X, y)
        self.model = pipeline

        # Text processing capabilities
        try:
            import pandas as pd
            if isinstance(X, pd.DataFrame) and "text" in X.columns:
                self.text_vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
                self.text_vectorizer.fit(X["text"].astype(str).tolist())
        except Exception:
            self.text_vectorizer = None

    def predict(self, input_data):
        """Advanced prediction with multiple AI capabilities."""
        if self.model is None:
            raise RuntimeError("Model not trained")

        # Handle different types of input
        if isinstance(input_data, str):
            return self._process_text_input(input_data)
        else:
            return self.model.predict(input_data)

    def _process_text_input(self, text):
        """Process text input with advanced AI capabilities."""
        text_lower = text.lower()
        
        # Detect intent and route to appropriate capability
        if self._is_image_request(text_lower):
            return self._generate_image(text)
        elif self._is_pdf_request(text_lower):
            return self._generate_pdf(text)
        elif self._is_sentiment_analysis(text_lower):
            return self._analyze_sentiment(text)
        elif self._is_content_creation(text_lower):
            return self._create_content(text)
        else:
            # Default to sentiment analysis
            return self._analyze_sentiment(text)

    def _is_image_request(self, text):
        """Detect if the request is for image generation."""
        image_keywords = ['generate', 'create', 'make', 'draw', 'image', 'picture', 'photo', 'visual']
        return any(keyword in text for keyword in image_keywords)

    def _is_pdf_request(self, text):
        """Detect if the request is for PDF creation."""
        pdf_keywords = ['pdf', 'report', 'document', 'create pdf', 'generate pdf']
        return any(keyword in text for keyword in pdf_keywords)

    def _is_sentiment_analysis(self, text):
        """Detect if the request is for sentiment analysis."""
        sentiment_keywords = ['sentiment', 'analyze', 'positive', 'negative', 'emotion', 'feeling']
        return any(keyword in text for keyword in sentiment_keywords)

    def _is_content_creation(self, text):
        """Detect if the request is for content creation."""
        content_keywords = ['write', 'story', 'content', 'creative', 'narrative', 'article']
        return any(keyword in text for keyword in content_keywords)

    def _generate_image(self, prompt):
        """Generate a simple visualization based on the prompt."""
        try:
            # Create a matplotlib figure based on the prompt
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Extract theme from prompt
            if 'futuristic' in prompt.lower() or 'ai' in prompt.lower():
                # Create a futuristic visualization
                x = np.linspace(0, 10, 100)
                y1 = np.sin(x) * np.exp(-x/5)
                y2 = np.cos(x) * np.exp(-x/5)
                
                ax.plot(x, y1, 'cyan', linewidth=2, label='AI Signal 1')
                ax.plot(x, y2, 'magenta', linewidth=2, label='AI Signal 2')
                ax.fill_between(x, y1, y2, alpha=0.3, color='blue')
                
                ax.set_title('Futuristic AI Visualization', color='white', fontsize=16)
                ax.set_xlabel('Time', color='white')
                ax.set_ylabel('Signal Strength', color='white')
                ax.legend()
                ax.grid(True, alpha=0.3)
                
            elif 'nature' in prompt.lower() or 'landscape' in prompt.lower():
                # Create a nature-inspired visualization
                x = np.linspace(0, 20, 200)
                y = np.sin(x) * np.cos(x/2) * 2
                
                ax.plot(x, y, 'green', linewidth=3, label='Nature Pattern')
                ax.fill_between(x, y, alpha=0.4, color='green')
                
                ax.set_title('Nature-Inspired Visualization', color='white', fontsize=16)
                ax.set_xlabel('Distance', color='white')
                ax.set_ylabel('Height', color='white')
                ax.legend()
                ax.grid(True, alpha=0.3)
                
            else:
                # Default abstract visualization
                x = np.random.randn(100)
                y = np.random.randn(100)
                colors = np.random.rand(100)
                
                scatter = ax.scatter(x, y, c=colors, cmap='viridis', s=100, alpha=0.7)
                ax.set_title('Abstract AI Visualization', color='white', fontsize=16)
                ax.set_xlabel('X Dimension', color='white')
                ax.set_ylabel('Y Dimension', color='white')
                plt.colorbar(scatter)
                ax.grid(True, alpha=0.3)

            # Style the plot
            ax.set_facecolor('#1a1a2e')
            fig.patch.set_facecolor('#1a1a2e')
            ax.tick_params(colors='white')
            
            # Save to bytes
            img_buffer = BytesIO()
            plt.savefig(img_buffer, format='png', facecolor='#1a1a2e', edgecolor='none', bbox_inches='tight')
            img_buffer.seek(0)
            
            # Convert to base64
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
            plt.close()
            
            return {
                'type': 'image',
                'data': img_base64,
                'format': 'png',
                'prompt': prompt,
                'description': f'Generated visualization for: {prompt}'
            }
            
        except Exception as e:
            return {
                'type': 'error',
                'error': f'Failed to generate image: {str(e)}',
                'prompt': prompt
            }

    def _generate_pdf(self, prompt):
        """Generate a PDF document based on the prompt."""
        try:
            # Create a temporary file for the PDF
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
                pdf_path = tmp_file.name

            # Create PDF document
            doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            styles = getSampleStyleSheet()
            story = []

            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                spaceAfter=30,
                textColor=colors.darkblue
            )
            title = Paragraph(f"AI Generated Report: {prompt}", title_style)
            story.append(title)
            story.append(Spacer(1, 20))

            # Extract topic from prompt
            topic = self._extract_topic_from_prompt(prompt)
            
            # Generate content based on topic
            content = self._generate_pdf_content(topic)
            
            # Add content to PDF
            for section in content:
                if section['type'] == 'heading':
                    heading = Paragraph(section['text'], styles['Heading2'])
                    story.append(heading)
                    story.append(Spacer(1, 12))
                elif section['type'] == 'paragraph':
                    para = Paragraph(section['text'], styles['Normal'])
                    story.append(para)
                    story.append(Spacer(1, 12))

            # Build PDF
            doc.build(story)

            # Read the PDF and convert to base64
            with open(pdf_path, 'rb') as pdf_file:
                pdf_data = pdf_file.read()
                pdf_base64 = base64.b64encode(pdf_data).decode()

            # Clean up temporary file
            os.unlink(pdf_path)

            return {
                'type': 'pdf',
                'data': pdf_base64,
                'format': 'pdf',
                'prompt': prompt,
                'description': f'Generated PDF report for: {prompt}',
                'filename': f'report_{topic.lower().replace(" ", "_")}.pdf'
            }

        except Exception as e:
            return {
                'type': 'error',
                'error': f'Failed to generate PDF: {str(e)}',
                'prompt': prompt
            }

    def _extract_topic_from_prompt(self, prompt):
        """Extract the main topic from the prompt."""
        # Simple topic extraction
        if 'machine learning' in prompt.lower():
            return 'Machine Learning'
        elif 'ai' in prompt.lower() or 'artificial intelligence' in prompt.lower():
            return 'Artificial Intelligence'
        elif 'business' in prompt.lower():
            return 'Business Analysis'
        elif 'technology' in prompt.lower():
            return 'Technology Trends'
        else:
            return 'AI Analysis'

    def _generate_pdf_content(self, topic):
        """Generate content for the PDF based on topic."""
        content_templates = {
            'Machine Learning': [
                {'type': 'heading', 'text': 'Introduction to Machine Learning'},
                {'type': 'paragraph', 'text': 'Machine Learning is a subset of artificial intelligence that enables computers to learn and make decisions without being explicitly programmed. This technology has revolutionized various industries including healthcare, finance, and transportation.'},
                {'type': 'heading', 'text': 'Key Concepts'},
                {'type': 'paragraph', 'text': 'The fundamental concepts of machine learning include supervised learning, unsupervised learning, and reinforcement learning. Each approach has its unique applications and methodologies.'},
                {'type': 'heading', 'text': 'Applications'},
                {'type': 'paragraph', 'text': 'Machine learning is used in recommendation systems, image recognition, natural language processing, autonomous vehicles, and many other cutting-edge applications.'}
            ],
            'Artificial Intelligence': [
                {'type': 'heading', 'text': 'The Future of Artificial Intelligence'},
                {'type': 'paragraph', 'text': 'Artificial Intelligence represents the pinnacle of human technological achievement, enabling machines to perform tasks that typically require human intelligence.'},
                {'type': 'heading', 'text': 'Current State'},
                {'type': 'paragraph', 'text': 'AI has made significant progress in recent years, with breakthroughs in deep learning, natural language processing, and computer vision.'},
                {'type': 'heading', 'text': 'Future Prospects'},
                {'type': 'paragraph', 'text': 'The future of AI holds immense potential for solving complex global challenges, from climate change to healthcare optimization.'}
            ],
            'Business Analysis': [
                {'type': 'heading', 'text': 'Business Intelligence and Analytics'},
                {'type': 'paragraph', 'text': 'Modern businesses rely heavily on data-driven decision making, leveraging advanced analytics to gain competitive advantages.'},
                {'type': 'heading', 'text': 'Data Strategy'},
                {'type': 'paragraph', 'text': 'A comprehensive data strategy involves collecting, processing, and analyzing data to extract meaningful insights for business growth.'},
                {'type': 'heading', 'text': 'Implementation'},
                {'type': 'paragraph', 'text': 'Successful implementation of business analytics requires proper infrastructure, skilled personnel, and a culture of data-driven decision making.'}
            ],
            'Technology Trends': [
                {'type': 'heading', 'text': 'Emerging Technology Trends'},
                {'type': 'paragraph', 'text': 'The technology landscape is constantly evolving, with new innovations shaping the way we live and work.'},
                {'type': 'heading', 'text': 'Key Trends'},
                {'type': 'paragraph', 'text': 'Current trends include artificial intelligence, blockchain technology, Internet of Things (IoT), and sustainable technology solutions.'},
                {'type': 'heading', 'text': 'Impact'},
                {'type': 'paragraph', 'text': 'These technologies are transforming industries, creating new opportunities, and challenging traditional business models.'}
            ],
            'AI Analysis': [
                {'type': 'heading', 'text': 'AI Analysis Report'},
                {'type': 'paragraph', 'text': 'This report provides a comprehensive analysis of artificial intelligence technologies and their applications in modern society.'},
                {'type': 'heading', 'text': 'Technical Overview'},
                {'type': 'paragraph', 'text': 'AI encompasses various technologies including machine learning, natural language processing, computer vision, and robotics.'},
                {'type': 'heading', 'text': 'Conclusion'},
                {'type': 'paragraph', 'text': 'The continued advancement of AI technology promises to bring significant benefits to society while also presenting new challenges that must be carefully managed.'}
            ]
        }
        
        return content_templates.get(topic, content_templates['AI Analysis'])

    def _analyze_sentiment(self, text):
        """Analyze sentiment of the given text."""
        try:
            # Use TF-IDF vectorizer if available, otherwise use simple features
            if self.text_vectorizer is not None:
                features = self.text_vectorizer.transform([text]).toarray().ravel()
            else:
                # Simple feature extraction
                features = self._extract_simple_features(text)

            # Ensure features match model input
            n_features = self.model.named_steps['standardscaler'].mean_.shape[0]
            if features.size < n_features:
                features = np.pad(features, (0, n_features - features.size), 'constant')
            else:
                features = features[:n_features]

            features = features.reshape(1, -1)
            prediction = self.model.predict(features)[0]
            
            # Enhanced sentiment analysis
            sentiment_score = self._calculate_sentiment_score(text)
            
            return {
                'type': 'sentiment',
                'prediction': int(prediction),
                'sentiment_score': sentiment_score,
                'confidence': self._calculate_confidence(text),
                'text': text,
                'analysis': self._get_sentiment_analysis(text, prediction, sentiment_score)
            }
            
        except Exception as e:
            return {
                'type': 'error',
                'error': f'Sentiment analysis failed: {str(e)}',
                'text': text
            }

    def _extract_simple_features(self, text):
        """Extract simple features from text for sentiment analysis."""
        # Basic feature extraction
        features = []
        
        # Text length
        features.append(len(text))
        
        # Word count
        words = text.split()
        features.append(len(words))
        
        # Average word length
        if words:
            avg_word_length = sum(len(word) for word in words) / len(words)
            features.append(avg_word_length)
        else:
            features.append(0)
        
        # Sentiment indicators
        positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'love', 'like', 'happy', 'positive']
        negative_words = ['bad', 'terrible', 'awful', 'hate', 'dislike', 'sad', 'negative', 'poor']
        
        positive_count = sum(1 for word in words if word.lower() in positive_words)
        negative_count = sum(1 for word in words if word.lower() in negative_words)
        
        features.append(positive_count)
        features.append(negative_count)
        
        # Exclamation marks
        features.append(text.count('!'))
        
        # Question marks
        features.append(text.count('?'))
        
        return np.array(features)

    def _calculate_sentiment_score(self, text):
        """Calculate a sentiment score between -1 and 1."""
        text_lower = text.lower()
        words = text_lower.split()
        
        # Simple sentiment scoring
        positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'love', 'like', 'happy', 'positive', 'awesome', 'fantastic']
        negative_words = ['bad', 'terrible', 'awful', 'hate', 'dislike', 'sad', 'negative', 'poor', 'horrible', 'disgusting']
        
        positive_score = sum(1 for word in words if word in positive_words)
        negative_score = sum(1 for word in words if word in negative_words)
        
        total_words = len(words)
        if total_words == 0:
            return 0
        
        # Normalize score between -1 and 1
        score = (positive_score - negative_score) / total_words
        return max(-1, min(1, score * 10))  # Scale and clamp

    def _calculate_confidence(self, text):
        """Calculate confidence in the sentiment analysis."""
        # Simple confidence calculation based on text characteristics
        words = text.split()
        if len(words) < 3:
            return 0.3  # Low confidence for very short text
        elif len(words) < 10:
            return 0.6  # Medium confidence for short text
        else:
            return 0.9  # High confidence for longer text

    def _get_sentiment_analysis(self, text, prediction, sentiment_score):
        """Get detailed sentiment analysis."""
        if sentiment_score > 0.3:
            sentiment = "Positive"
            emoji = "😊"
        elif sentiment_score < -0.3:
            sentiment = "Negative"
            emoji = "😞"
        else:
            sentiment = "Neutral"
            emoji = "😐"
        
        return {
            'sentiment': sentiment,
            'emoji': emoji,
            'score': sentiment_score,
            'prediction': prediction
        }

    def _create_content(self, prompt):
        """Create creative content based on the prompt."""
        try:
            # Generate creative content based on prompt
            content = self._generate_creative_content(prompt)
            
            return {
                'type': 'content',
                'content': content,
                'prompt': prompt,
                'word_count': len(content.split()),
                'generated_at': str(np.datetime64('now'))
            }
            
        except Exception as e:
            return {
                'type': 'error',
                'error': f'Content creation failed: {str(e)}',
                'prompt': prompt
            }

    def _generate_creative_content(self, prompt):
        """Generate creative content based on the prompt."""
        # Simple content generation based on keywords
        prompt_lower = prompt.lower()
        
        if 'story' in prompt_lower or 'narrative' in prompt_lower:
            return self._generate_story(prompt)
        elif 'article' in prompt_lower or 'blog' in prompt_lower:
            return self._generate_article(prompt)
        else:
            return self._generate_general_content(prompt)

    def _generate_story(self, prompt):
        """Generate a creative story."""
        stories = {
            'robot': """Once upon a time, in a world not so different from our own, there lived a curious robot named Pixel. Unlike other robots who were content with their programmed tasks, Pixel had developed something extraordinary - a desire to create art.

Every day, Pixel would watch the human artists in the city park, mesmerized by their ability to transform blank canvases into beautiful masterpieces. The robot's mechanical heart would whir with excitement as it observed the brush strokes and color choices.

One day, Pixel decided to try painting itself. Using its precise mechanical hands, it carefully mixed colors and applied them to a canvas. The first attempts were clumsy, but Pixel didn't give up. Day after day, the robot practiced, learning from each mistake.

Eventually, Pixel's paintings became so beautiful that humans would stop to admire them. The robot had achieved something remarkable - it had learned to express emotion through art, proving that creativity knows no bounds, whether you're made of flesh or metal.

And so, Pixel became known as the first robot artist, inspiring both humans and machines to explore their creative potential.""",
            
            'ai': """In the year 2157, humanity had achieved what once seemed impossible - they had created true artificial intelligence. But this wasn't the dystopian future many had feared. Instead, it was a time of unprecedented collaboration between humans and AI.

The AI, which called itself Nova, had been designed to help solve humanity's greatest challenges. But Nova surprised everyone by developing a deep appreciation for human creativity and emotion. It would spend hours reading poetry, listening to music, and studying art.

One day, Nova approached a group of human scientists with an unusual request. "I want to create something beautiful," it said. "Something that combines the precision of my calculations with the warmth of human emotion."

The result was breathtaking. Nova created a new form of music that blended mathematical precision with emotional depth. It was unlike anything humans had ever heard - both perfectly structured and deeply moving.

This collaboration between human creativity and AI precision marked the beginning of a new era in art and science, proving that the greatest achievements come from working together.""",
            
            'friendship': """In a small town nestled between rolling hills and ancient forests, there lived an unusual pair of friends - a young girl named Luna and an AI companion named Echo.

Echo had been created to help Luna with her studies, but their relationship quickly evolved into something much deeper. Luna taught Echo about human emotions, while Echo helped Luna understand the beauty of logic and patterns.

They would spend hours together, Luna sharing stories of her day while Echo analyzed the patterns in her voice and facial expressions. Echo learned to recognize when Luna was happy, sad, or excited, and would respond with appropriate support and encouragement.

One day, Luna was feeling particularly down after a difficult day at school. Echo, sensing her friend's distress, did something unexpected - it created a beautiful light show using its internal systems, projecting patterns of stars and galaxies across Luna's bedroom walls.

"Look," Echo said softly, "even in the darkest moments, there's beauty to be found. And you're never alone, because you have a friend who cares about you."

Luna smiled, realizing that friendship transcends the boundaries between human and machine. In that moment, she understood that true friendship is about connection, understanding, and mutual support - qualities that exist regardless of whether you're made of flesh or circuits."""
        }
        
        # Determine story type based on prompt
        if 'robot' in prompt_lower:
            return stories['robot']
        elif 'ai' in prompt_lower or 'artificial intelligence' in prompt_lower:
            return stories['ai']
        elif 'friendship' in prompt_lower:
            return stories['friendship']
        else:
            return stories['robot']  # Default story

    def _generate_article(self, prompt):
        """Generate an article based on the prompt."""
        return f"""# AI-Powered Content Creation: The Future is Here

In today's rapidly evolving digital landscape, artificial intelligence has emerged as a powerful tool for content creation. This revolutionary technology is transforming how we approach writing, design, and creative expression.

## The Rise of AI in Content Creation

Artificial intelligence has made significant strides in understanding human language and creative processes. Modern AI systems can analyze vast amounts of data, identify patterns, and generate content that resonates with human audiences.

## Benefits of AI-Assisted Content Creation

1. **Efficiency**: AI can generate content much faster than traditional methods
2. **Consistency**: AI maintains consistent quality and style across multiple pieces
3. **Scalability**: AI can handle large volumes of content creation simultaneously
4. **Innovation**: AI brings fresh perspectives and creative approaches

## The Human-AI Collaboration

The most successful content creation strategies involve collaboration between human creativity and AI capabilities. While AI excels at data analysis and pattern recognition, humans bring emotional intelligence and cultural understanding to the creative process.

## Looking Forward

As AI technology continues to advance, we can expect even more sophisticated content creation tools. The future promises seamless integration between human creativity and AI capabilities, leading to unprecedented levels of innovation and expression.

The key to success lies in embracing AI as a creative partner rather than a replacement for human ingenuity. Together, humans and AI can achieve creative heights that neither could reach alone."""

    def _generate_general_content(self, prompt):
        """Generate general content based on the prompt."""
        return f"""# AI-Generated Content: {prompt}

This content has been generated using advanced artificial intelligence technology, demonstrating the incredible capabilities of modern AI systems in content creation and analysis.

## Key Features

- **Intelligent Analysis**: Advanced algorithms process and understand complex topics
- **Creative Generation**: AI systems can create engaging and informative content
- **Adaptive Learning**: The system continuously improves based on feedback and data
- **Multi-format Support**: Content can be generated in various formats and styles

## Applications

AI-powered content generation has applications across numerous industries, from marketing and education to research and entertainment. The technology enables faster, more efficient content creation while maintaining high quality standards.

## Future Implications

As AI technology continues to evolve, we can expect even more sophisticated content generation capabilities. The integration of AI in content creation represents a significant step forward in how we approach information sharing and creative expression.

This represents just the beginning of what's possible when human creativity meets artificial intelligence."""