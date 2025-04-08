from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', password='password123'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', password='password123'),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', password='password123'),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', password='password123'),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', password='password123'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Blue Team', members=[user.id for user in users[:3]]),
            Team(name='Gold Team', members=[user.id for user in users[3:]]),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date='2025-04-01'),
            Activity(user=users[1], type='Running', duration=45, date='2025-04-02'),
            Activity(user=users[2], type='Swimming', duration=30, date='2025-04-03'),
            Activity(user=users[3], type='Strength Training', duration=50, date='2025-04-04'),
            Activity(user=users[4], type='Yoga', duration=40, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=teams[0], points=150),
            Leaderboard(team=teams[1], points=200),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Endurance cycling workout'),
            Workout(name='Running Training', description='Interval running workout'),
            Workout(name='Swimming Training', description='Freestyle swimming workout'),
            Workout(name='Strength Training', description='Full-body strength workout'),
            Workout(name='Yoga Session', description='Relaxing yoga session'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))