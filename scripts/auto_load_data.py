#!/usr/bin/env python3
"""
Auto Load Data Script - Simple one-command data loading
Automatically populates PostgreSQL with sample data for RDI testing
"""

import os
import time
import random
import psycopg2

# Database configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "chinook")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

def connect_to_db():
    """Connect to PostgreSQL database"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"❌ Failed to connect to database: {e}")
        print("💡 Make sure PostgreSQL is running: docker-compose up -d postgres")
        return None

def auto_populate_data():
    """Automatically populate database with sample data"""
    print("🎵 Auto-loading sample data for RDI testing...")
    
    conn = connect_to_db()
    if not conn:
        return False
    
    cursor = conn.cursor()
    
    try:
        # Sample data
        artists = [
            "The Beatles", "Led Zeppelin", "Pink Floyd", "Queen", "The Rolling Stones",
            "AC/DC", "Metallica", "Nirvana", "Radiohead", "U2", "Coldplay", "Red Hot Chili Peppers"
        ]
        
        albums = [
            "Abbey Road", "Led Zeppelin IV", "The Dark Side of the Moon", "A Night at the Opera",
            "Sticky Fingers", "Back in Black", "Master of Puppets", "Nevermind", "OK Computer",
            "The Joshua Tree", "Parachutes", "Blood Sugar Sex Magik"
        ]
        
        tracks = [
            "Come Together", "Stairway to Heaven", "Money", "Bohemian Rhapsody", "Paint It Black",
            "Thunderstruck", "Enter Sandman", "Smells Like Teen Spirit", "Paranoid Android",
            "Where the Streets Have No Name", "Yellow", "Under the Bridge", "Imagine", 
            "Hotel California", "Sweet Child O' Mine", "Billie Jean", "Like a Rolling Stone", 
            "Hey Jude", "Purple Haze", "Wonderwall", "Creep", "Black", "Alive", "Jeremy",
            "One", "Master of Puppets", "Back in Black", "Highway to Hell", "We Will Rock You"
        ]
        
        composers = [
            "Lennon-McCartney", "Jimmy Page", "Roger Waters", "Freddie Mercury", "Mick Jagger",
            "Angus Young", "James Hetfield", "Kurt Cobain", "Thom Yorke", "Bono", "Chris Martin"
        ]
        
        # Clear existing data
        print("  🧹 Clearing existing data...")
        cursor.execute("DELETE FROM Track")
        cursor.execute("DELETE FROM Album") 
        cursor.execute("DELETE FROM Artist")
        
        # Reset sequences
        cursor.execute("ALTER SEQUENCE artist_artistid_seq RESTART WITH 1")
        cursor.execute("ALTER SEQUENCE album_albumid_seq RESTART WITH 1")
        cursor.execute("ALTER SEQUENCE track_trackid_seq RESTART WITH 1")
        
        # Load Artists
        print("  🎤 Loading artists...")
        for i, artist_name in enumerate(artists, 1):
            cursor.execute("""
                INSERT INTO Artist (ArtistId, Name) VALUES (%s, %s)
            """, (i, artist_name))
        
        # Load Albums
        print("  💿 Loading albums...")
        for i, album_title in enumerate(albums, 1):
            artist_id = random.randint(1, len(artists))
            cursor.execute("""
                INSERT INTO Album (AlbumId, Title, ArtistId) VALUES (%s, %s, %s)
            """, (i, album_title, artist_id))
        
        # Load Tracks
        print("  🎵 Loading tracks...")
        for i, track_name in enumerate(tracks, 1):
            album_id = random.randint(1, len(albums))
            composer = random.choice(composers)
            milliseconds = random.randint(180000, 360000)  # 3-6 minutes
            bytes_size = random.randint(3000000, 8000000)  # 3-8 MB
            unit_price = round(random.uniform(0.99, 1.99), 2)
            genre_id = random.randint(1, 5)
            
            cursor.execute("""
                INSERT INTO Track (TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice) 
                VALUES (%s, %s, %s, 1, %s, %s, %s, %s, %s)
            """, (i, track_name, album_id, genre_id, composer, milliseconds, bytes_size, unit_price))
        
        conn.commit()
        
        # Show final counts
        cursor.execute("SELECT COUNT(*) FROM Artist")
        artist_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM Album")
        album_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM Track")
        track_count = cursor.fetchone()[0]
        
        print(f"\n✅ Data loaded successfully!")
        print(f"  🎤 Artists: {artist_count}")
        print(f"  💿 Albums: {album_count}")
        print(f"  🎵 Tracks: {track_count}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def generate_continuous_data():
    """Generate new tracks continuously"""
    print("\n🔄 Starting continuous data generation...")
    print("   (This will add new tracks every 3-8 seconds)")
    print("   Press Ctrl+C to stop\n")
    
    conn = connect_to_db()
    if not conn:
        return
    
    track_names = [
        "Acoustic Version", "Live Version", "Remix", "Extended Mix", "Radio Edit",
        "Unplugged", "Demo Version", "Alternate Take", "Remastered", "Director's Cut"
    ]
    
    composers = [
        "Lennon-McCartney", "Jimmy Page", "Roger Waters", "Freddie Mercury", "Mick Jagger",
        "Angus Young", "James Hetfield", "Kurt Cobain", "Thom Yorke", "Bono", "Chris Martin"
    ]
    
    try:
        counter = 0
        while True:
            cursor = conn.cursor()
            
            # Get next track ID
            cursor.execute("SELECT COALESCE(MAX(TrackId), 0) + 1 FROM Track")
            next_id = cursor.fetchone()[0]
            
            # Generate track
            base_name = random.choice(["Rock Anthem", "Power Ballad", "Heavy Metal", "Pop Hit", "Classic Rock"])
            version = random.choice(track_names)
            track_name = f"{base_name} {next_id} ({version})"
            
            album_id = random.randint(1, 12)
            composer = random.choice(composers)
            milliseconds = random.randint(180000, 360000)
            bytes_size = random.randint(3000000, 8000000)
            unit_price = round(random.uniform(0.99, 1.99), 2)
            genre_id = random.randint(1, 5)
            
            cursor.execute("""
                INSERT INTO Track (TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice) 
                VALUES (%s, %s, %s, 1, %s, %s, %s, %s, %s)
            """, (next_id, track_name, album_id, genre_id, composer, milliseconds, bytes_size, unit_price))
            
            conn.commit()
            cursor.close()
            
            counter += 1
            print(f"  ➕ [{counter:3d}] Added track {next_id}: {track_name}")
            
            # Wait 3-8 seconds
            wait_time = random.randint(3, 8)
            time.sleep(wait_time)
            
    except KeyboardInterrupt:
        print(f"\n🛑 Stopped after generating {counter} tracks")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        conn.close()

def main():
    print("🚀 Redis RDI Training - Auto Data Loader")
    print("=" * 45)
    
    # Auto-populate initial data
    if auto_populate_data():
        print("\n🎯 Ready for RDI testing!")
        print("\nOptions:")
        print("  • Start RDI now to sync this data to Redis")
        print("  • Run continuous generation for live testing")
        
        response = input("\nGenerate continuous data? (y/N): ").strip().lower()
        if response in ['y', 'yes']:
            generate_continuous_data()
        else:
            print("\n✅ Initial data loaded. You can run this script again anytime!")
            print("💡 To generate continuous data later: python3 auto_load_data.py")

if __name__ == "__main__":
    main()
