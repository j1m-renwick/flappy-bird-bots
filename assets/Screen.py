class Screen:


    def __init__(self, screen, baseline):
        self.screen = screen
        self.baseline = baseline

    def assess_death(self, bird, pipes):

        if bird.ypos + bird.sprite.get_height() >= self.baseline \
                or bird.ypos < 0:
            return True

        for pipe_pair in pipes:
            # if collided
            if bird.X_POS + bird.sprite_width >= pipe_pair.xpos \
                    and bird.X_POS < pipe_pair.xpos + pipe_pair.sprite_width \
                    and not (bird.ypos > pipe_pair.gap_start and bird.ypos + bird.sprite_height < pipe_pair.gap_end):
                return True

        return False

    def get_next_pipe(self, bird, pipes):
        best_pipe = None
        # TODO refactor to remove this hardcoding
        best_dist = 10000
        for pipe_pair in pipes:
            dist = pipe_pair.xpos + pipe_pair.sprite_width - bird.X_POS + bird.sprite_width
            if 0 < dist < best_dist:
                best_dist = dist
                best_pipe = pipe_pair

        return best_pipe