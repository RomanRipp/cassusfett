from unittest import TestCase
from unittest.mock import Mock
from brain import Brain, WalkState, RestState, solve_distance, OBSTACLE, DROP, NORMAL


class TestBrain(TestCase):
    def test_run_brain(self):
        mock_tracks = Mock()
        mock_sonar = Mock()
        mock_light = Mock()
        brain = Brain(mock_tracks, mock_sonar, mock_light)
        brain.run()
        mock_tracks.stop.assert_called_once()
        mock_sonar.start.assert_called_once()
        mock_light.start.assert_called_once()

    def test_die_brain(self):
        mock_tracks = Mock()
        mock_sonar = Mock()
        mock_light = Mock()
        brain = Brain(mock_tracks, mock_sonar, mock_light)
        brain.die()
        mock_tracks.stop.assert_called_once()
        mock_sonar.stop.assert_called_once()
        mock_light.stop.assert_called_once()

    def test_rest_light_off(self):
        mock_tracks = Mock()
        brain = Brain(mock_tracks, Mock(), Mock())
        brain.on_light_change(False)
        mock_tracks.forward.assert_called_once()
        self.assertIsInstance(brain._current_state, WalkState)

    def test_rest_light_on(self):
        mock_tracks = Mock()
        brain = Brain(mock_tracks, Mock(), Mock())
        brain.on_light_change(True)
        mock_tracks.assert_not_called()
        self.assertIsInstance(brain._current_state, RestState)

    def test_rest_distance_changed(self):
        mock_tracks = Mock()
        brain = Brain(mock_tracks, Mock(), Mock())
        brain.on_distance_change(42.0)
        mock_tracks.assert_not_called()
        self.assertIsInstance(brain._current_state, RestState)

    def test_walk_light_off(self):
        mock_tracks = Mock()
        brain = Brain(mock_tracks, Mock(), Mock())
        brain._current_state = WalkState(mock_tracks)
        brain.on_light_change(False)
        mock_tracks.assert_not_called()
        self.assertIsInstance(brain._current_state, WalkState)

    def test_walk_light_on(self):
        mock_tracks = Mock()
        brain = Brain(mock_tracks, Mock(), Mock())
        brain._current_state = WalkState(mock_tracks)
        brain.on_light_change(True)
        mock_tracks.stop.assert_called_once()
        self.assertIsInstance(brain._current_state, RestState)

    def test_walk_obstacle(self):
        mock_tracks = Mock()
        brain = Brain(mock_tracks, Mock(), Mock())
        brain._current_state = WalkState(mock_tracks)
        brain.on_distance_change(42.0)
        mock_tracks.backward.assert_called_once()
        mock_tracks.forward.assert_called_once()
        self.assertIsInstance(brain._current_state, WalkState)

    # TODO separate sensor is needed for that
    # def test_walk_drop(self):
    #     mock_tracks = Mock()
    #     brain = Brain(mock_tracks, Mock(), Mock())
    #     brain._current_state = WalkState(mock_tracks)
    #     brain.on_distance_change(142.0)
    #     mock_tracks.backward.assert_called_once()
    #     mock_tracks.forward.assert_called_once()
    #     self.assertIsInstance(brain._current_state, WalkState)

    def test_walk_normal(self):
        mock_tracks = Mock()
        brain = Brain(mock_tracks, Mock(), Mock())
        brain._current_state = WalkState(mock_tracks)
        brain.on_distance_change(101.0)
        mock_tracks.assert_not_called()
        self.assertIsInstance(brain._current_state, WalkState)

    def test_distance(self):
        res = solve_distance(42)
        self.assertEqual(res, OBSTACLE)
        res = solve_distance(142)
        self.assertEqual(res, DROP)
        res = solve_distance(101)
        self.assertEqual(res, NORMAL)







