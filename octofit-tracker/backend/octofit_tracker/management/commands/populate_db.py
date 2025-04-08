from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', password='password123'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', password='password123'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', password='password123'),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff', password='password123'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(_id=ObjectId(), name='Blue Team', members=[user._id for user in users[:3]]),
            Team(_id=ObjectId(), name='Gold Team', members=[user._id for user in users[3:]]),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], type='Cycling', duration=60, date='2025-04-01'),
            Activity(_id=ObjectId(), user=users[1], type='Running', duration=45, date='2025-04-02'),
            Activity(_id=ObjectId(), user=users[2], type='Swimming', duration=30, date='2025-04-03'),
            Activity(_id=ObjectId(), user=users[3], type='Strength Training', duration=50, date='2025-04-04'),
            Activity(_id=ObjectId(), user=users[4], type='Yoga', duration=40, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=teams[0], points=150),
            Leaderboard(_id=ObjectId(), team=teams[1], points=200),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Endurance cycling workout'),
            Workout(_id=ObjectId(), name='Running Training', description='Interval running workout'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Freestyle swimming workout'),
            Workout(_id=ObjectId(), name='Strength Training', description='Full-body strength workout'),
            Workout(_id=ObjectId(), name='Yoga Session', description='Relaxing yoga session'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
